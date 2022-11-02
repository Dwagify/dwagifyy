import time

# Console Colorer
class bcolors:
  RESET = '\033[0m'
  WARNING = '\033[33m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  CYAN = '\033[36m'

# Delayer
class wait:
  # Seconds
  def sec(seconds):
    time.sleep(seconds)
    return seconds

  # Minutes
  def min(minutes):
    minute = minutes * 60
    time.sleep(minute)
    return minutes

