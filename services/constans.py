import os 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#json file path defined as a constant
dataPath = os.path.join('data','data.json')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#User: Edwin
#password: secret

fake_users_db = {
    "Edwin": {
        "username": "Edwin",
        "full_name": "Edwin Puertas",
        "email": "epuerta@utb.edu.co",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}