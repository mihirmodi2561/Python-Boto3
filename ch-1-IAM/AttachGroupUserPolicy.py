# Ch:21
import boto3

def attach_group_user_policy(policy_arns,group_name):
    iam = boto3.client('iam')

    for policy_arn in policy_arns:
        response = iam.attach_group_policy(
        GroupName= group_name,
        PolicyArn= policy_arn
        )
    
        print(f"GroupName: {group_name} \nPolicyArn: {policy_arns}")

# List of policy ARNs
policies = [
    'arn:aws:iam::aws:policy/AmazonRDSFullAccess',
    'arn:aws:iam::aws:policy/AmazonS3FullAccess',
    'arn:aws:iam::aws:policy/AWSLambda_FullAccess',
    'arn:aws:iam::aws:policy/AmazonEC2FullAccess',
    'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess',
    # Add more ARNs as needed
]

attach_group_user_policy(policies, 'RDSUser')