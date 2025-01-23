# Ch 22

import boto3

def addUserToGroupUser(groupname, username):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
    GroupName= groupname,
    UserName= username
)
    
    print(response)

addUserToGroupUser('RDSUser', 'update-name')


