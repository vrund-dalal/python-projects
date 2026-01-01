import time

print("Simple Alarm Clock")

seconds = int(input("Set alarm after how many seconds? "))

while seconds > 0:
    print("Time left:", seconds, "seconds")
    time.sleep(1)
    seconds -= 1

print("⏰ WAKE UP! ⏰")
