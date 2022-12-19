# py-event-bus

Super simple event bus in Python 3, built with asyncio. No decorators required. Built around a subset of the NodeJS [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) API. 

A PyPI package implementating this as a module can be found [here](https://pypi.org/project/event-emitter-asyncio/).

A full write up and explanation can be found [here](https://joeltok.com/blog/2021-3/building-an-event-bus-in-python).

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

## Development Setup

```sh
git clone git@github.com:joeltok/py-event-bus.git
cd ./py-event-bus
python3 -m venv ./venv
source venv/bin/activate
pip3 install pytest
pip3 install pytest-asyncio
```

## Testing 

```sh
python3 -m pytest event_bus/ event_bus_advanced_examples/
```
