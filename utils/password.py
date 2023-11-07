from passlib.context import CryptContext

# Create a CryptContext object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hash a password
def hashPassword(password):
    hashed_password = pwd_context.hash(password)
    return hashed_password


# Verify a password
def verifyPassword(password, hashPassword):
    is_verified = pwd_context.verify(password, hashPassword)
    return is_verified
