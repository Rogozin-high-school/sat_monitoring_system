from . import config
#Returns the ratio of the the distance passed by the satellite in the given time
def get_ratio(time:float)->float:
	return (time % config.CIRCLE_TIME) / config.CIRCLE_TIME

# Returns the location of the satellite in the form of angle after given time
def get_angle(time:float)->float:
    return 360 * get_ratio(time)
