from carbonfootprint import logger
from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
from carbonfootprint.pipeline.Stage_02_Data_Validation import DataValidationPipeline
from carbonfootprint.pipeline.Stage_03_Data_Transformation import DataTransformationPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} ++++++++++++")
    data_injestion = DataIngestionPipeline()
    data_injestion.ingestion()
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++") 
    data_validation = DataValidationPipeline()
    data_validation.validation()
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e