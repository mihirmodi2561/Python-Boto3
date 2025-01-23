import boto3

def attach_policy_users(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

    print(response)

attach_policy_users('arn:aws:iam::205930615550:policy/pythonFullAccess', 'update-name')

