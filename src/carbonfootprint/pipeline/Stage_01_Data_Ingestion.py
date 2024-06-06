from carbonfootprint import logger
from carbonfootprint.components.Data_Ingestion import DataIngestion
from carbonfootprint.components.Data_Ingestion import DataIngestionException

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def ingestion(self):
        try:
            injestion = DataIngestion()
            raw_data_path = injestion.initiate_data_ingestion()
            logger.info(f"Data ingested and saved to {raw_data_path}")
        except DataIngestionException as e:
            logger.error(f"An error occurred during data ingestion: {e}")


if __name__ == "__main__":
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} ++++++++++++")
        data_injestion = DataIngestionPipeline()
        data_injestion.ingestion()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++")
    except DataIngestionException as e:
        logger.error(f"An error occurred during data ingestion: {e}")