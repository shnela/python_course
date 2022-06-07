"""
Result (macOS, python3.9):
    Class dict used 268.587008 MB.
    Class EventSlots used 107.298816 MB.
    Class EventTuple used 123.6992 MB.
    Class Event used 218.939392 MB.
    Class EventDataclass used 219.15648 MB.
"""
import os
import random
from collections import namedtuple
from multiprocessing import Pool
from dataclasses import dataclass

import psutil

DNA_BASES = 'ATCG'


class Event:
    def __init__(self, dna_base, value):
        self.dna_base = dna_base
        self.value = value


@dataclass
class EventDataclass:
    # https://docs.python.org/3/library/dataclasses.html
    dna_base: str
    value: int


class EventSlots:
    # https://book.pythontips.com/en/latest/__slots__magic.html
    # https://docs.python.org/3/reference/datamodel.html?highlight=__slots__#object.__slots__
    __slots__ = ['dna_base', 'value']

    def __init__(self, dna_base, value):
        self.dna_base = dna_base
        self.value = value


# https://www.geeksforgeeks.org/namedtuple-in-python/
EventTuple = namedtuple('EventTuple', ['dna_base', 'value'])


def generate_events(event_cls: type, events_no: int = 10 ** 6):
    events = [
        event_cls(dna_base=random.choice(DNA_BASES), value=i)
        for i in range(events_no)
    ]
    process = psutil.Process(os.getpid())
    process_size = process.memory_info().rss / 10 ** 6  # in MB
    print(f"Class {event_cls.__name__} used {process_size} MB.")


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(generate_events, [dict, Event, EventSlots, EventTuple, EventDataclass])
