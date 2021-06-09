import os
import re
import time
import subprocess
import threading
from time import sleep
from threading import Timer

class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False
    
    def hello(name):
    print "Hello %s!" % name

print "Starting to repeat the process..."
RRepeater = RepeatedTimer(3, hello, "World") # it auto-starts, no need of rt.start()
try:
    sleep(10)# your long-running job goes here...
    print "Hello Maysam!"
finally:
    RRepeater.stop() # better in a try/finally block to make sure the program ends!

#noderesources = {}
#nodecpuc = os.cpu_count{}
#noderesources = {'cpucores'} = nodecpuc
