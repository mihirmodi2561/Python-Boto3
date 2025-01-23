import boto3

def all_policy():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    # Local or AWS or ALl we can write in Scope
    for response in paginator.paginate(Scope='Local'): 
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            policy_arn = policy['Arn']

            print(f"Policy Name: {policy_name} \nPolicy ARN: {policy_arn}")

all_policy()