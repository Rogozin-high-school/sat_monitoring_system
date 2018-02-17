#!/usr/bin/python

import sys
import os

arguments = sys.argv

if len(arguments) != 2:
    print("Please specify only the test name and nothing else")

test_name = arguments[1]

os.chdir("../")
os.system("python -m sat_monitoring_system.Tests." + test_name)
