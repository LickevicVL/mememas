from datetime import datetime
from time import time

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
YEAR = DAY * 365

NEW = 'new'
HOT = 'hot'


class TimeAgo:
    NOW = 'just now'
    MINUTES_AGO = '{} minute(s) ago'
    HOURS_AGO = '{} hour(s) ago'
    DAYS_AGO = '{} day(s) ago'
    YEARS_AGO = '{} years ago'

    @classmethod
    def get_time_ago(cls, date: datetime):
        delta = time() - date.timestamp()

        if 0 < delta < MINUTE:
            return cls.NOW

        if MINUTE < delta < HOUR:
            return cls.MINUTES_AGO.format(int(delta / MINUTE))

        if HOUR < delta < DAY:
            return cls.HOURS_AGO.format(int(delta / HOUR))

        if DAY < delta < YEAR:
            return cls.DAYS_AGO.format(int(delta / DAY))

        return cls.YEARS_AGO.format(int(delta / YEAR))
