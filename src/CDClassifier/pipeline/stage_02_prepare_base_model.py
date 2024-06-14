from CDClassifier.config.configuration import ConfigurationManager
from CDClassifier.components.prepare_base_model import PrepareBaseModel
from CDClassifier import logger

STAGE_NAME = "Prepare Base Model stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        logger.info(f">>> stage {STAGE_NAME} completed <<<")

if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} complated <<<")
    except Exception as e:
        logger.exception(e)
        raise e