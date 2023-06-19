from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier.logging import logger

STAGE_NAME = 'model evaluation'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':

    try:
        logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
        prepare_base_model = ModelEvaluationTrainingPipeline()
        prepare_base_model.main()
        logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

    except Exception as e:
        logger.exception(e)
        raise e