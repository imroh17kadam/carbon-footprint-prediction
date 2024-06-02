from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Model_Evaluation import ModelEvaluation
from carbonfootprint import logger



STAGE_NAME = "Model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        obj = ModelEvaluationPipeline()
        obj.evaluation()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e