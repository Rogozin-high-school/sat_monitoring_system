# Satellite Monitoring System
SMS is a web app written in python. The web app would display reading and sensor data collected by the satellite.  
SMS will be hosted on the satellite, currently a Raspberry Pi Zero W running Raspbian.

## Structure
Please maintain the repo's structure and organization when commiting to the repo.  
The structure of the repo is as follows :
* ```Modules/``` - This directory contains all of the software and hardware modules of the system.  
* ```Tests/``` - This directory contains one or more tests for each software and  
hardware modules. See the Tests section on why this is needed.
* ```Applications/``` - This directory contains the main code files for the different experiments, the code
that links between all of the modules.
* ```run_test.py``` - A script for easily running the tests, pass it the paramter "pi" after the file name if you run
it on a raspberry pi.
* ```run_applications.py``` - A script for easily running applications, pass it the paramter "pi" after the file name if you run
it on a raspberry pi.

## Contributions
If you would like to contribute to the sat_monitoring_system  
please fork our repo and write all of your code in the forked repo.
When you finished working on your code open a pull request to merge your commits into our repo.  
When opening your pull request please describe as well as you can what is the purpose of your  
commits and the purpose of the pull request.

## Tests
When writing a software module please write a test for the module as well.  
The tests are intended to make sure the software works as intended and handles  
input correctly.  
When writing a test plesae add it to the ```Tests``` folder.  
In order to run a test please run ```test.py``` and pass it the name of the  
script you wish to run.

## Contribution Guidelines
Please follow the following guidelines when contributing to our repo.
* __Naming__ - Please follow [PEP8](https://www.python.org/dev/peps/pep-0008/) when writing your code to insure consistent naming.
* __Comments__ - Don't forget to comment your code (classes, methods, variables, etc...).  
Please use docstrings in your code as described in [PEP257](https://www.python.org/dev/peps/pep-0257/).
* __Testing__ - If you add something new to one of the modules please add examples in the module's test,  
that way we could just run the test, see that everything is good and works as intended.
