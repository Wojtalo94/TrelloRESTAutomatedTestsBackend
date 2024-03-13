from tools.RestController import RestController
import logging


logging.basicConfig(filename="logs/logs_rest.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("Enviornment")


def before_all(context):
    logger.info('BEFORE ALL START')
    logger.info('BEFORE ALL END')


def before_feature(context, feature):
    logger.info('BEFORE FEATURE START')
    context.rest_controller = RestController()
    logger.info('BEFORE FEATURE END')