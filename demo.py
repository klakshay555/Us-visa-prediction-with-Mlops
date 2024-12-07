from Us_visa.logger import logging
from Us_visa.exception import UsVisaException
import sys

#logging.info("this is a test for custom log")

try:
    a = 2/0
except Exception as e:
    raise UsVisaException(e,sys)