import pynecone as pc
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_url = os.getenv('API_URL')
backend_port = os.getenv('BACKEND_PORT')

config = pc.Config(
    app_name='plot_gms',
    api_url=api_url,
    backend_port=backend_port,
    db_url='sqlite:///pynecone.db',
    env=pc.Env.DEV,
)
