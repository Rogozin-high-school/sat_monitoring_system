import os

SAT = SATELLITE = PROD = PRODUCTION = os.name == "posix"
DEBUG = os.name == "nt"