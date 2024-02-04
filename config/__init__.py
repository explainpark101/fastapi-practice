from .settings import app

@app.get("/")
def main():
    return {"message": "Hello, World!"}