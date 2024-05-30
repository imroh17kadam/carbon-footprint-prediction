import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from carbonfootprint import logger


# Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'ingestion', 'data.csv')



class DataIngestionException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def read_data(self, file_path):
        """
        Read the dataset from the specified file path.

        Args:
            file_path (str): The path to the dataset file.

        Returns:
            pd.DataFrame: The loaded dataset.
        """
        try:
            logger.info(f"Reading data from {file_path}")
            df = pd.read_csv(file_path)
            logger.info('Dataset loaded into DataFrame')
            return df
        except Exception as e:
            logger.error(f"Error reading data from {file_path}: {e}")
            raise DataIngestionException(f"Error reading data from {file_path}", e)


    def save_data(self, df, save_path):
        """
        Save the DataFrame to the specified file path.

        Args:
            df (pd.DataFrame): The DataFrame to save.
            save_path (str): The path to save the DataFrame.
        """
        try:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            df.to_csv(save_path, index=False, header=True)
            logger.info(f"Data saved to {save_path}")
        except Exception as e:
            logger.error(f"Error saving data to {save_path}: {e}")
            raise DataIngestionException(f"Error saving data to {save_path}", e)


    def initiate_data_ingestion(self):
        """
        Orchestrate the data ingestion process.
        """
        logger.info("Entered the data ingestion method or component")
        try:
            source_file_path = 'c:\\Users\\Admin\\Desktop\\Rohit\\MachineLearning\\ml-mlops-workflow\\src\\carbonfootprint\\dataset\\CarbonFootprintData.csv'
            df = self.read_data(source_file_path)
            self.save_data(df, self.ingestion_config.raw_data_path)
            logger.info("Data ingestion process completed")
            return self.ingestion_config.raw_data_path
        except Exception as e:
            logger.error(f"Data ingestion failed: {e}")
            raise DataIngestionException("Data ingestion process failed", e)