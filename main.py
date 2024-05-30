from carbonfootprint import logger
from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline
# from carbonfootprint.pipeline.Stage_01_Data_Ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"++++++++++++ stage {STAGE_NAME} ++++++++++++")
    obj = DataIngestionPipeline()
    obj.ingestion()
    logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++")
except Exception as e:
    logger.exception(e)
    raise e