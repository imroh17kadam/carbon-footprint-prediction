import os
from carbonfootprint import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from carbonfootprint.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def catrgorical_encoding(self):
        self.df = pd.read_csv(self.config.data_path)

        cat_features = ['Transmission', 'Fuel Type']
        self.df_new = self.df.drop(columns=cat_features)

        # Apply One-Hot Encoding using str.get_dummies() for each categorical feature
        for feature in cat_features:
            dummies = self.df[feature].str.get_dummies()
            df_new = pd.concat([self.df_new, dummies.add_prefix(feature + '_')], axis=1)

        columns_to_drop = ['Make', 'Model', 'Vehicle Class']
        self.df_new = self.df_new.drop(columns=columns_to_drop)
        self.df_new.shape


    def standariztion(self):
        pass


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(self.df_new)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)