from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Model_Evaluation import ModelEvaluation
from carbonfootprint import logger



STAGE_NAME = "Model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def evaluation(self, y_test, y_test_pred, y_train, y_train_pred):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow(y_test, y_test_pred, y_train, y_train_pred)



if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.evaluation()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e