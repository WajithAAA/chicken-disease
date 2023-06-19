from cnnClassifier.logging import logger
from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipelines.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'data ingestion stage'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'prepare base model'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e