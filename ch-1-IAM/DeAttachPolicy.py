import boto3

iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName= 'update-name',
    PolicyArn='string'
)

print(response)


