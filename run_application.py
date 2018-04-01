#!/usr/bin/python

import sys
import os

arguments = sys.argv

if len(arguments) == 2:
    test_name = arguments[1]

    os.chdir("../")
    os.system("py -3 -m sat_monitoring_system.Applications." + test_name)

elif len(arguments) == 3:
    if arguments[2] == "pi":
        test_name = arguments[1]

        os.chdir("../")
        os.system("python3 -m sat_monitoring_system.Applications." + test_name)
