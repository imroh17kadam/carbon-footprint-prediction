from carbonfootprint import logger
from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
from carbonfootprint.pipeline.Stage_02_Data_Validation import DataValidationPipeline
from carbonfootprint.pipeline.Stage_03_Data_Transformation import DataTransformationPipeline
from carbonfootprint.pipeline.Stage_04_Model_Trainer import ModelTrainerPipeline
from carbonfootprint.pipeline.Stage_05_Model_Evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} ++++++++++++")
    data_injestion = DataIngestionPipeline()
    data_injestion.ingestion()
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e


# STAGE_NAME = "Data Validation stage"
# try:
#     logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++") 
#     data_validation = DataValidationPipeline()
#     data_validation.validation()
#     logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
    data_transformation = DataTransformationPipeline()
    scaled_x_train_arr, scaled_x_test_arr = data_transformation.transformation()
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n") 
    model_trainer = ModelTrainerPipeline()
    y_test, y_test_pred, y_train, y_train_pred = model_trainer.trainer(scaled_x_train_arr, scaled_x_test_arr)
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n") 
   model_evaluation = ModelEvaluationPipeline()
   model_evaluation.evaluation(y_test, y_test_pred, y_train, y_train_pred)
   logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n")
except Exception as e:
    logger.exception(e)
    raise e