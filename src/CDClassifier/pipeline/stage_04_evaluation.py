from CDClassifier.config.configuration import ConfigurationManager
from CDClassifier.components.evaluation import Evaluation
from CDClassifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        logger.info("Evaluation saved")

if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<< \n\n-----------------")
    except Exception as e:
        logger.exception(e)
        raise e