import pytest
from decoder_exercise_solution import Decoder


@pytest.fixture
def decoder():
    yield Decoder()
