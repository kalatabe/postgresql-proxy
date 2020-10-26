import logging
import random
from time import sleep

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('intercept')


def handle_query(query, context):
    how_long = random.randint(5, 15)
    logger.info('*yawn*... feeling sleepy, taking a break for %s seconds...', how_long)
    sleep(how_long)
    return query
