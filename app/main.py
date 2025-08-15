from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.common.logger import logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Starting app...")
    yield
    logger.info("Stopping app...")


app = FastAPI(lifespan=lifespan)
