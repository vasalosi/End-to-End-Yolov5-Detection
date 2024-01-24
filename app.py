from EmergencyDetection.logger import logging
from EmergencyDetection.exception import AppException
import sys

try:
    a = 3 / "s"
except Exception as e:
    raise AppException(e, sys)


#logging.info("Welcome to my custom log")