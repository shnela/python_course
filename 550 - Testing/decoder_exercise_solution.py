import enum
from functools import wraps
from random import random
from time import sleep


class DecoderException(Exception):
    pass


class State(enum.Enum):
    standby = 'STANDBY'
    on = 'ON'


class ResolutionChoice(enum.Enum):
    hd = 'HD'
    full_hd = 'FHD'


class Server:
    def check_payment(self):
        sleep(1)
        val = random()
        return val > 0.1


def do_not_operate_on_standby(f):
    """Probably no better way of doing it
    https://stackoverflow.com/a/11731208/1565454
    """
    @wraps(f)
    def inner_func(self, *args, **kwargs):
        if self._state == State.standby:
            raise DecoderException
        return f(self, *args, **kwargs)

    return inner_func


class Decoder:
    def __init__(self):
        self._resolution = ResolutionChoice.hd
        self._current_channel = 1
        self._state = State.standby
        self._server = Server()
        self._blocked = False

    def check_payment(self):
        payment_ok = self._server.check_payment()
        if not payment_ok:
            self._blocked = True

    def is_blocked(self):
        return self._blocked

    @do_not_operate_on_standby
    def set_resolution(self, resolution: ResolutionChoice) -> None:
        self._resolution = resolution

    @do_not_operate_on_standby
    def get_resolution(self) -> ResolutionChoice:
        return self._resolution

    @do_not_operate_on_standby
    def set_channel(self, channel: int) -> None:
        if channel <= 0:
            raise DecoderException
        self._current_channel = channel

    def get_current_channel(self) -> int:
        return self._current_channel

    def turn_off(self):
        self._state = State.standby

    def turn_on(self):
        self._state = State.on

    def get_state(self) -> State:
        return self._state

    @do_not_operate_on_standby
    def channel_up(self):
        self._current_channel += 1

    @do_not_operate_on_standby
    def channel_down(self):
        if self._current_channel == 1:
            raise DecoderException

        self._current_channel -= 1
