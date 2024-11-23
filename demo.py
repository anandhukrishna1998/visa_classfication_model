from us_visa.logger import logging
import sys
import us_visa.exception as USvisaException

logging.info ("Testing the logging message")



try:
    a=1/0
except Exception as e:
    raise USvisaException(e, sys.exc_info())