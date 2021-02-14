# py-event-bus

Super simple event bus in Python 3, built with asyncio. No decorators required. Built around a subset of the NodeJS [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) API. 

## Usage

```python
from py_event_bus.EventBus import EventBus
event_bus = EventBus()

async def func(event):
  for pet in event['pets']:
    print(pet)
  
event_data = {
  'pets': ['cats', 'dogs']  
}
event_bus.add_listener('some-event', func)
event_bus.emit('some-event', event_data)
event_bus.remove_listener('some-event', func)
```

This will give:
```sh
> cats
> dogs
```
