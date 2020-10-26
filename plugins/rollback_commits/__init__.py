import re
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('intercept')

# The field to replace
field_pattern = re.compile('COMMIT;?', re.IGNORECASE)


def rewrite_query(query, context):
    logger.info(query)
    replace = 'ROLLBACK;'
    if re.match(field_pattern, query):
        logger.info('Commit detected, converting it to a rollback...')
        return field_pattern.sub(replace, query)

    return query
