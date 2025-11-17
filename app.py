from src.project_all.logger import logger
from src.project_all.exception import customExeption
import sys

logger.info("Training pipeline started")
logger.warning("Missing values found in dataset")
logger.error("Model failed to train")


if __name__ == "__main__":
    logger.info("execution started")
    try:
        # jkhn
        x = 2/0
    except Exception as e:
        logger.info("error in exception")
        raise customExeption(e, sys)