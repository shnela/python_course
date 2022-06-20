import enum


__all__ = [
    'DecoderException',
    'Decoder',
    'State',
    'ResolutionChoice'
]


class DecoderException(Exception):
    pass


class State(enum.Enum):
    standby = 'STANDBY'
    on = 'ON'


class ResolutionChoice(enum.Enum):
    hd = 'HD'
    full_hd = 'FHD'


class Decoder:
    pass
