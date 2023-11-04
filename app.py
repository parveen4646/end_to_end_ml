import sys
sys.path.append('/Users/Guchi/Documents/projects/endtoendmlproject/')
from src.endtoend.logger import logging
from src.endtoend.exception import CustomException
from src.endtoend.components.data_ingestion import DataIngestionConfig,DataIngestion
import os

from src.endtoend.components.data_transformation import DataTransformatioConfig,DataTransformatio
from src.endtoend.components.model_trainer import ModelTrainerConfig,ModelTrainer

if __name__=="__main__":
    logging.info("execution started")
    try:
        data_ingestion=DataIngestion()
        logging.info('test,train')
        train,test,raw=data_ingestion.initiate_data_Ingestion()
        logging.info('test,train imported')

        data_transformation=DataTransformatio()
        logging.info('now')
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train,test)
        ##model training
        modeltrainer=ModelTrainer()
        acc,clp=modeltrainer.initiate_model_trainer(train_arr,test_arr)
        
        print(clp)
        


        
    except Exception as e:
        logging.info('gadbad h')
        raise CustomException(e,sys)      