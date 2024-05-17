import datetime

from .time_converter import iso_format_to_unix_time


DAYS_OF_THE_WEEK = 7


def current_week_start(of=None):

    date_to_compare = datetime.datetime.now()

    if of is not None:

        date_to_compare = datetime.datetime.utcfromtimestamp(of)

    current_weekday_starting_in_one = date_to_compare.weekday() + 1

    sunday_time_delta = datetime.timedelta(current_weekday_starting_in_one % DAYS_OF_THE_WEEK)

    sunday = date_to_compare - sunday_time_delta

    sunday_without_time = sunday.date()

    return iso_format_to_unix_time(sunday_without_time.isoformat())


def previous_week_start(of=None):

    current_sunday = datetime.datetime.utcfromtimestamp(current_week_start(of))

    previous_sun = (current_sunday - datetime.timedelta(DAYS_OF_THE_WEEK)).date()

    return iso_format_to_unix_time(previous_sun.isoformat())
