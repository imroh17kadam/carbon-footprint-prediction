from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Model_Trainer import ModelTrainer
from carbonfootprint import logger
from pathlib import Path



STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()




if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        obj = ModelTrainerPipeline()
        obj.trainer()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e