from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Model_Trainer import ModelTrainer
from carbonfootprint import logger
from pathlib import Path



STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def trainer(self, scaled_train_array, scaled_test_array):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        y_test, y_test_pred, y_train, y_train_pred = model_trainer_config.train(scaled_train_array, scaled_test_array)
        return(y_test, y_test_pred, y_train, y_train_pred)




if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        model_trainer = ModelTrainerPipeline()
        model_trainer.trainer()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e