import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

# DATABASE
DB_NAME = env('POSTGRES_DB')
DB_USER = env('POSTGRES_USER')
DB_PASSWORD = env('POSTGRES_PASSWORD')
DB_HOST = env('POSTGRES_HOST')
DB_PORT = env('POSTGRES_PORT')

DB_NAME_TEST = 'test_db'
DB_USER_TEST = 'test_user'
DB_PASSWORD_TEST = 'root'
DB_HOST_TEST = env('POSTGRES_HOST')
DB_PORT_TEST = env('POSTGRES_PORT')

URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

JWT_SECRET = env('JWT_SECRET')
ALGORITHM = env('ALGORITHM')

# MAIL_USERNAME = env('MAIL_USERNAME')
# MAIL_PASSWORD = env('MAIL_PASSWORD')
# MAIL_FROM = env('MAIL_FROM')
# MAIL_PORT = env('MAIL_PORT')
# MAIL_SERVER = env('MAIL_SERVER')
# MAIL_FROM_NAME = env('MAIL_FROM_NAME')

CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379/1')

QUICKNODE_URL = env('QUICKNODE_URL', default='')
MORALIS_API_KEY = env('MORALIS_API_KEY', default='')

ALLOWED_HOSTS = ['http://127.0.0.1:8000']


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
BUCKET = env('BUCKET')

RABBITMQ_URL = env('RABBITMQ_URL')

WIRING_CONFIG = [
    'src.auth',
    'src.users',
    'src.blog',
    'src.card',
    'src.core',
]

DATABASE_TEST_URL = f'postgresql+asyncpg://{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}'
