from pyfirmata import Arduino, util
import time

board = Arduino("COM3")

loopTimes = input('How many time would you like LED to blink')
print("Blinking"  + looptimes + "times")

for x in range(int(loopTimes)):
  board.digital[13].write(1)
  time.sleep(1)
  board.digital[13].write(0)
  time.sleep(1)
