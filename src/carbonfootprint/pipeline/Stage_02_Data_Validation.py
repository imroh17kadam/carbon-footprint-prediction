from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Data_Validation import DataValidation
from carbonfootprint import logger


STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init__(self):
        pass


    def validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        validation = DataValidation(config=data_validation_config)
        validation.validate_all_columns()



if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        data_validation = DataValidationPipeline()
        data_validation.validation()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e