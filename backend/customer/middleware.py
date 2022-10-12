import jwt

key = "fucking_secret_key"
algorithm = "HS256"


def sign_token(user):
    encoded = jwt.encode(user, key, algorithm)
    return encoded


def verify(encoded):
    decoded = jwt.decode(encoded, key, algorithm)
    return decoded




