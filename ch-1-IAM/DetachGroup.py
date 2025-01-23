import boto3

def detach_group(group_name, arn):
    iam = boto3.client('iam')

    response = iam.detach_policy(
        GroupName = group_name,
        PolicyArn = arn
    )

    print(response)

detach_group()


