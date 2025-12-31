# exeption class checking
from sensor.execption import SensorExeption
import sys
from sensor.logger import logging

if __name__ == "__main__":
    try:
        logging.info("[dividong by zero not allowed]")
        a = 1/0
    except Exception as e:
        raise SensorExeption(e, sys)