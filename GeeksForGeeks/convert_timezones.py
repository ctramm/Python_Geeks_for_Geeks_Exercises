from datetime import datetime, timezone


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


start_time = datetime.utcnow()
end_time = datetime.now()

start_time2 = utc_to_local(start_time)


print(start_time)
print(start_time2)
print(end_time)
result = start_time < end_time
assert result
