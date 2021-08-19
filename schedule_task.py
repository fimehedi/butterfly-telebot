import time
import datetime
import schedule
from module.bot import Bot, config

SCHEDULE_TIME = config['SCHEDULE_TIME']
GROUP_ID = config['GROUP_ID']

def send_message(text):
    Bot.send_message(GROUP_ID, text)

# Schedule Task
schedule.every().saturday.at(SCHEDULE_TIME).do(send_message, config['SAT_ROUTINE'])
schedule.every().sunday.at(SCHEDULE_TIME).do(send_message, config['SUN_ROUTINE'])
schedule.every().monday.at(SCHEDULE_TIME).do(send_message, config['MON_ROUTINE'])
schedule.every().tuesday.at(SCHEDULE_TIME).do(send_message, config['TUE_ROUTINE'])
schedule.every().wednesday.at(SCHEDULE_TIME).do(send_message, config['WED_ROUTINE'])
schedule.every().thursday.at(SCHEDULE_TIME).do(send_message, config['THU_ROUTINE'])
schedule.every().friday.at(SCHEDULE_TIME).do(send_message, config['FRI_MSG'])

# Sleep until schedule time is reached
def sleep_until(hour, minute):
    t = datetime.datetime.now()
    future = datetime.datetime(t.year, t.month, t.day, hour, minute)
    if t.hour >= hour:
        future += datetime.timedelta(days=1)
    print((future - t).total_seconds())
    time.sleep((future - t).total_seconds())

def main():
    while True:
        schedule_hour = int(SCHEDULE_TIME.split(':')[0])
        schedule_min = int(SCHEDULE_TIME.split(':')[1])

        sleep_until(schedule_hour, schedule_min)
        schedule.run_pending()


if __name__ == "__main__":
    main()