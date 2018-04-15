from . import config
'''
Input - the time passed from measurement start
Output - the ratio of the route that the satellite has already passed
'''
def get_ratio(time:float)->float:
	return (time % config.CIRCLE_TIME) / config.CIRCLE_TIME

'''
Input - the time passed from measurement start
Output - the location of the satellite on the route in the form of angle
'''
def get_angle(time:float)->float:
    return 360 * get_ratio(time)
