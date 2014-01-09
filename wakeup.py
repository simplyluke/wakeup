#!/usr/bin/env python3

from datetime import datetime, timedelta

def get_wakeups():
  # Avg sleep cycle is 1.5 hours
  sleep_cycles = [3, 4.5, 6, 7.5, 9, 10.5]
  # Takes a person ~ 15 minutes to fall asleep
  account_for_falling = datetime.now() + timedelta(minutes=15)

  wakeup_times = []
  for i in sleep_cycles:
    wakeup_times.append(account_for_falling + timedelta(hours=i))

  return wakeup_times

def print_wakeups(times):
  print("You should get up at one of the following times:")
  for x in times:
    print('{:%I:%M %p}'.format(x))

if __name__ == '__main__':
  print_wakeups(get_wakeups())
