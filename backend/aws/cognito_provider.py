import boto3


class CognitoProvider:

    def __init__(self):
        self.client = boto3.client('cognito-idp')

    def create_user(self, new_user):
        self.client.admin_create_user(

            UserPoolId='string',
            Username='string',
            UserAttributes=[
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            ValidationData=[
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            TemporaryPassword='string',
            ForceAliasCreation=False,
            MessageAction='RESEND',
            DesiredDeliveryMediums=['EMAIL'],
            ClientMetadata={
                'string': 'string'
            }
        )
