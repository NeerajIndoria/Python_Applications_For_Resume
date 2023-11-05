# Reminder Application with Notification
from plyer import notification
# import time
from datetime import datetime


def water_reminder():
    notification.notify(
        title="Water Reminder",
        message="Go and Keep yourself Hydrated",
        app_icon="D:\Python100\Codes\Projects Resume\Reminder_App\icon.ico",
        timeout=10
    )


def lunch_reminder():
    notification.notify(
        title="Lunch Time",
        message="Go and get some food",
        timeout=10
    )


def snacks_reminder():
    notification.notify(
        title="Snacks Time",
        message="It's time for Snacks",
        timeout=10
    )


def to_do_list():
    notification.notify(
        title="Prepare To-Do list",
        message="Its time to prepare list for todays work.",
        timeout=10
    )


if __name__ == "__main__":
    while True:
        CURRENT_TIME = datetime.now()
        EXACT_TIME = CURRENT_TIME.strftime("%H:%M:%S")

        if EXACT_TIME == "10:00:00":
            to_do_list()
        if EXACT_TIME == "12:30:00":
            lunch_reminder()
        if EXACT_TIME == "02:40:00":
            snacks_reminder()
        if EXACT_TIME == "02:41 :00":
            snacks_reminder()
