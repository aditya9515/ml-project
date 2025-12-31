# exeption class checking
from sensor.execption import SensorExeption
import sys

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        print(SensorExeption(e, sys))