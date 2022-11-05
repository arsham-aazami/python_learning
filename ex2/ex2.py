# Student name : Arsham Aazami
# Student code : 4012061003

def seconds_difference(time_1, time_2):
	""" (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
	return time_2 - time_1


def hours_difference(time_1, time_2):
	""" (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
	hours_diff = float((time_2 - time_1) / 3600)
	return hours_diff


def to_float_hours(hours, minutes, seconds):
	""" (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.
    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
	if 0 <= minutes <= 60 and 0 <= seconds <= 60:
		min_to_hour = minutes / 60
		sec_to_hour = seconds / 3600
		total_hours = hours + min_to_hour + sec_to_hour
		return float(total_hours)


def to_24_hour_clock(hours):
	""" (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """
	if hours >= 0:
		return hours % 24


### Write your get_hours function definition here:
hour = 0


def get_hours(seconds):
	'''
    (int) -> int
    :param seconds:
    :return: The time which has been converted to hours from second
    '''
	hour = seconds // 3600
	return hour


### Write your get_minutes function definition here:

minute = 0


def get_minutes():
	'''

	:return: The time in minute after passing one or more hours
	'''
	minute = (3800 - (3600 * get_hours(3800))) // 60
	return minute


### Write your get_seconds function definition here:
def get_seconds():
	'''

	:return: The time in second after passing one or more hours
	'''
	second = (3800 - (3600 * get_hours(3800)) - get_minutes() * 60)
	return second

def time_to_utc(utc_offset, time):
	""" (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
	hours_away = time - utc_offset
	utc_time = hours_away % 24
	return utc_time


def time_from_utc(utc_offset, time):
	""" (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
	converted_time = time + utc_offset
	if converted_time < 0:
		converted_time += 24
	return converted_time
