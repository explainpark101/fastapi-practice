import fastapi
import pathlib

BASE_DIR = pathlib.Path(__name__).resolve().parent
DEBUG = True
PORT = 8080

app = fastapi.FastAPI()