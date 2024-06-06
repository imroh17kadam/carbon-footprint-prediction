from carbonfootprint.config.configuration import ConfigurationManager
from carbonfootprint.components.Data_Transformation import DataTransformation
from carbonfootprint import logger
from pathlib import Path



STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass


    def transformation(self):
        try:
            # with open(Path("c:\\Users\\Admin\\Desktop\\Rohit\\MachineLearning\\ml-mlops-workflow\\artifacts\\data_validation\\status.txt"), "r") as f:
            #     status = f.read().split(" ")[-1]

            status = "True"
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                transformation = DataTransformation(config=data_transformation_config)
                transformation.catrgorical_encoding()
                transformation.train_test_spliting()
                scaled_x_train_arr, scaled_x_test_arr = transformation.standardization()
                return(scaled_x_train_arr, scaled_x_test_arr)
            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)

 
if __name__ == '__main__':
    try:
        logger.info(f"++++++++++++ stage {STAGE_NAME} started ++++++++++++\n\nx=========================================================x\n")
        data_transformation = DataTransformationPipeline()
        data_transformation.transformation()
        logger.info(f"++++++++++++ stage {STAGE_NAME} completed ++++++++++++\n\nx=========================================================x\n\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e