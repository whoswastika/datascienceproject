from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

# logger.info("welcome to our cusom hehehe")

# class DataTransformation:
#     def __init__(self,config:DataTransformationConfig):
#         self.config = config
        
        
#     def train_test_splitting(self):
#         data=pd.read_csv(self.config.data_path)
        
#         train,test= train_test_split(data)
        
#         train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
#         test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index= False)
        
#         logger.info("Splitted Data into training and testing")
#         logger.info(train.shape)
#         logger.info(test.shape)
        
#         print(train.shape)
#         print(test.shape)
        
        

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
       

STAGE_NAME = "Data Validation Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
         
         
STAGE_NAME = "Model Training Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.initiate_model_training()
    logger.info(f"<<<<< stage {STAGE_NAME} completed<<<<<< \n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
    
    
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<<")
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.initate_model_evaluation()
    logger.info(f"<<<<< stage {STAGE_NAME} completed<<<<<< \n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
    
