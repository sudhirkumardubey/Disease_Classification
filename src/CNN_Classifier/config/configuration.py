# to read yaml files
from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories

from CNN_Classifier.entity.config_entity import DataIngestionConfig

"""
update constants/__init__.py
use function from utils.common.py
use config/config.yaml 

"""
# reads yaml files 
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # Make sure that yaml files are not empty
        self.config = read_yaml(config_filepath)
        # print(self.config)
        self.params = read_yaml(params_filepath) 
        # print(self.params) 

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # creating variable name, data_ingestion from config.yaml

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config