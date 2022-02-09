from datetime import timedelta
class Config:
    JWT_SECRET_KEY = 'super-secret'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=4)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
