import boto3


def create_user_group(group_name):
    iam = boto3.client('iam')

    response = iam.create_group(
        GroupName= group_name
    )

    print(response)

create_user_group("RDSUser")