# Satellite Monitoring System
SMS is a web app written in python. The web app would display reading and sensor data collected by the satellite.  
SMS will be hosted on the satellite, currently a Raspberry Pi 3 Model B running Raspbian.

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
When writing a test plesae add it to the ```Modules/Tests``` folder. When running it please  
run the following command from the main folder (the one containing ```main.py```) :  
```python -m Modules.Tests.<test_name_without_extension>```

## Contribution Guidelines
Please follow the following guidelines when contributing to our repo.
* __Naming__ - Please follow [PEP8](https://www.python.org/dev/peps/pep-0008/) when writing your code to insure consistent naming.
* __Comments__ - Don't forget to comment your code (classes, methods, variables, etc...).  
Please use docstrings in your code as described in [PEP257](https://www.python.org/dev/peps/pep-0257/).
* __Testing__ - If you add something new to one of the modules please add examples in the module's test,  
that way we could just run the test, see that everything is good and works as intended.
