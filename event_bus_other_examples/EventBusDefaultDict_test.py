import pytest
import asyncio

from event_bus_advanced_examples.EventBusDefaultDict import EventBusDefaultDict

@pytest.mark.asyncio
async def test_subscribe_remove_and_emit():
  a_first_events = []
  a_second_events = []
  b_first_events = []

  async def a_first(event_data): a_first_events.append(event_data)
  async def a_second(event_data): a_second_events.append(event_data)
  async def b_first(event_data): b_first_events.append(event_data)

  event_bus = EventBusDefaultDict()
  event_bus.add_listener('a', a_first)
  event_bus.add_listener('a', a_second)
  event_bus.add_listener('b', b_first)

  event_one = {}
  event_bus.emit('a', event_one)
  await asyncio.sleep(0.1)

  assert len(a_first_events) == 1
  assert a_first_events[0] == event_one
  assert len(a_second_events) == 1
  assert a_second_events[0] == event_one
  assert len(b_first_events) == 0

  event_two = {}
  event_bus.emit('b', event_two)
  await asyncio.sleep(0.1)
  assert len(a_first_events) == 1
  assert len(a_second_events) == 1
  assert len(b_first_events) == 1
  assert b_first_events[0] == event_two

  event_bus.remove_listener('b', b_first)
  event_three = {}
  event_bus.emit('b', event_three)
  await asyncio.sleep(0.1)
  assert len(b_first_events) == 1

  event_bus.remove_listener('a', a_first)
  event_four = {}
  event_bus.emit('a', event_four)
  await asyncio.sleep(0.1)
  assert len(a_first_events) == 1
  assert len(a_second_events) == 2
  assert a_second_events[0] == event_four
