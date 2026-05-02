import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from content_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from content_summarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from content_summarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from content_summarization.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from content_summarization.logging import logger

RUN_MODEL_TRAINER = False


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
if RUN_MODEL_TRAINER:
   try:
      logger.info(f"*******************")
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      from content_summarization.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
      model_trainer = ModelTrainerTrainingPipeline()
      model_trainer.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
           logger.exception(e)
           raise e
else:
   logger.info(f">>>>>> stage {STAGE_NAME} skipped (using pre-trained model files) <<<<<<")




STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e





