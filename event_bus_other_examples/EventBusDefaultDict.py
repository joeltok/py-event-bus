import asyncio
from collections import defaultdict
    
class EventBusDefaultDict():
  def __init__(self):
    self.listeners = defaultdict(set)

  def add_listener(self, event_name, listener):
    self.listeners[event_name].add(listener)

  def remove_listener(self, event_name, listener):
    self.listeners[event_name].remove(listener)
    if len(self.listeners[event_name]) == 0:
      del self.listeners[event_name]

  def emit(self, event_name, event):
    listeners = self.listeners.get(event_name, [])
    for listener in listeners:
      asyncio.create_task(listener(event))
