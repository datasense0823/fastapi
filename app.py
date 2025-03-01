from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Ensure the root path ("/") is defined
def home():
    return {"message": "Hello, FastAPI! 🚀 Your app is live!. I am learning something"}

@app.get("/health")  # Optional health check endpoint
def health_check():
    return {"status": "healthy"}
