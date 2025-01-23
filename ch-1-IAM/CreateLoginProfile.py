# Ch 25
import boto3

def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        UserName= username,
        Password= 'python@123',
        PasswordResetRequired= False
    )

    print(login_profile)

create_login("python-boto3-user")