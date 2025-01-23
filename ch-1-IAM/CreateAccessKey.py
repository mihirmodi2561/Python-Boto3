import boto3

def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
    UserName = username
)
    print(response)

create_access('update-name')

''' '''

def update_access_key():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId = '',
        Status = '', # Active or Inactive
        UserName = '' 
    )

update_access_key()