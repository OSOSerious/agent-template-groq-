import uvicorn
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting AgentGPT server...")
    uvicorn.run(
        "src.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
