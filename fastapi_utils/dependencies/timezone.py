import timezones
from fastapi import Header


def timezone(x_timezone: str = Header(None, description="Timezone")):
    tz = x_timezone or timezones.get_default_timezone_name()

    try:
        timezones.activate(tz)
        yield tz
    finally:
        timezones.deactivate()
