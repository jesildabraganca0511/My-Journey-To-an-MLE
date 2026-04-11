import boto3 
import json
from botocore.exceptions import ClientError


#Define client
iam=boto3.client("iam",region_name="us-east-1")


#get users
def list_iam_users():

    try:
        paginator= iam.get_paginator("list_users")

        print(f"{'Username':<30} {'User ID':<22} {'Created'}")

        for page in paginator.paginate():
            for user in page['Users']:
                print(f"{user['UserName']:<30} {user['UserId']:<22} {user['CreateDate'].strftime('%Y-%m-%d')}")
   
    except ClientError as e:
        code =e.response['Error']['Code']
        msg=e.response['Error']['Message']