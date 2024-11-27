import boto3
from moto import mock_aws


@mock_aws
def test_foobar():
    c_idp = boto3.client("cognito-idp")
    username = "developer@example.com"
    user_pool_id, pool_client_id = _setup_cognito(c_idp)
    access_token = create_cognito_user_and_get_access_token(
        c_idp, user_pool_id, pool_client_id, username
    )


def _setup_cognito(c_idp):
    """
    Setup Cognito User Pool and Client, and create a user with a temporary password.
    """

    res = c_idp.create_user_pool(
        PoolName="foobar-api-test-user-pool",
        Policies={
            "PasswordPolicy": {
                "MinimumLength": 8,
                "RequireUppercase": False,
                "RequireLowercase": False,
                "RequireNumbers": False,
                "RequireSymbols": False,
                "TemporaryPasswordValidityDays": 7,
            }
        },
    )
    user_pool_id = res["UserPool"]["Id"]
    res = c_idp.create_user_pool_client(
        UserPoolId=user_pool_id,
        ClientName="foobar-api-test-client",
        ExplicitAuthFlows=["ALLOW_USER_PASSWORD_AUTH"],
    )
    client_id = res["UserPoolClient"]["ClientId"]
    return user_pool_id, client_id


def create_cognito_user_and_get_access_token(
    c_idp, user_pool_id, pool_client_id, username
):
    """
    Create a user in Cognito User Pool and get an access token for it.
    """

    res = c_idp.admin_create_user(
        UserPoolId=user_pool_id,
        Username=username,
        UserAttributes=[
            {"Name": "email", "Value": username},
        ],
        TemporaryPassword="Password123",
    )
    res = c_idp.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=pool_client_id,
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": "Password123",
        },
    )

    res = c_idp.admin_respond_to_auth_challenge(
        UserPoolId=user_pool_id,
        ClientId=pool_client_id,
        ChallengeName="NEW_PASSWORD_REQUIRED",
        ChallengeResponses={
            "USERNAME": username,
            "NEW_PASSWORD": "Password1234",
        },
        Session=res["Session"],
    )

    access_token = res["AuthenticationResult"]["AccessToken"]
    return access_token
