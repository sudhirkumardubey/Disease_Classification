from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.data_ingestion import DataIngestion
from CNN_Classifier import logger


STAGE_NAME = "Data Ingestion Stage"


# Lets create pipeline 
class DataIngestionTrainingPipeline:
    def __init__(self): # it will be empty since we dont define any variable here
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config() #get_data_ingestion_config
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    
        
# since indicating dvc thats why defining as such
# if not using dvc we have to call this in our main.py
    
if __name__ == "__main__":

    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
        
    

