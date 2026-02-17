# dates.py

from datetime import datetime, date, timedelta, timezone


def demo_current_date_time():
    now = datetime.now()
    today = date.today()
    print("Current datetime:", now)
    print("Today's date:", today)


def demo_create_date():
    custom_date = date(2026, 2, 17)
    custom_datetime = datetime(2026, 2, 17, 15, 30)
    print("Custom date:", custom_date)
    print("Custom datetime:", custom_datetime)


def demo_formatting():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d"))
    print(now.strftime("%d.%m.%Y %H:%M"))


def demo_date_difference():
    d1 = datetime(2026, 2, 17)
    d2 = datetime(2026, 2, 25)
    difference = d2 - d1
    print("Days difference:", difference.days)


def demo_timezone():
    utc_time = datetime.now(timezone.utc)
    print("UTC time:", utc_time)


if __name__ == "__main__":
    demo_current_date_time()
    demo_create_date()
    demo_formatting()
    demo_date_difference()
    demo_timezone()
