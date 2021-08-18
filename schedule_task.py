import time
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

def job():
    print("working")

schedule.every(2).seconds.do(job)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()