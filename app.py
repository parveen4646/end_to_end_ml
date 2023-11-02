from src.endtoend.logger import logging
from src.endtoend.exception import CustomException
from src.endtoend.components.data_ingestion import DataIngestionConfig,DataIngestion
import os
import sys
sys.path.append('/Users/Guchi/Documents/projects/endtoendmlproject/')

if __name__=="__main__":
    logging.info("execution started")
    try:
        data_ingestion=DataIngestion()
    except Exception as e:
        raise CustomException(str(e)) from e        