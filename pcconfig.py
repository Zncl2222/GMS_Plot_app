import pynecone as pc
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

api_url = os.getenv('API_URL')
frontend_port = os.getenv('FRONTEND_PORT')
backend_port = os.getenv('BACKEND_PORT')
mode = os.getenv('MODE')

bun_path = '/app/.bun/bin/bun' if mode == 'PROD' else pc.constants.BUN_PATH

config = pc.Config(
    app_name='plot_gms',
    api_url=api_url,
    port=frontend_port,
    bun_path=bun_path,
    backend_port=backend_port,
    db_url='sqlite:///pynecone.db',
)
