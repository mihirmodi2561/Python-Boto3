import boto3

def update_user(old_username, new_username):
    iam = boto3.client('iam')

    response = iam.update_user(
        NewUserName= new_username,
        UserName= old_username
    )

    print(response)

update_user('test_user','update-name')