from fastapi import FastAPI
from app.middleware.security import SecurityHeadersMiddleware

app = FastAPI(title="SentinelAPI", version="0.1.0")
app.add_middleware(SecurityHeadersMiddleware)

@app.get("/")
async def root():
    return {"message": "SentinelAPI Operational"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
