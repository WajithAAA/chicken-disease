from cnnClassifier.logging import logger
from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'DATA_INGESTION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e