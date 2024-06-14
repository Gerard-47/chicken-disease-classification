from src.CDClassifier import logger

from CDClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from CDClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CDClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from CDClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"********************************")
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} complated <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Pipeline"
try:
    logger.info(f"**********************")
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} complated <<< \n\n-----------------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation Pipeline"
try:
    logger.info(f"********************************")
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<< \n\n-----------------")
except Exception as e:
    logger.exception(e)
    raise e