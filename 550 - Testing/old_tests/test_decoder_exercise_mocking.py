import unittest
from unittest.mock import patch

from decoder_exercise_solution import *


class TestDecoder(unittest.TestCase):
    decoder = None

    def setUp(self) -> None:
        self.decoder = Decoder()

    def test_check_payment_noblock(self):
        # given
        self.decoder.turn_on()

        # when
        with patch.object(Server, 'check_payment', return_value=True) as mocked_payment:
            self.decoder.check_payment()

        # then
        self.assertFalse(self.decoder.is_blocked())

    def test_check_payment_block(self):
        # given
        self.decoder.turn_on()

        # when
        with patch.object(Server, 'check_payment', return_value=False) as mocked_payment:
            self.decoder.check_payment()

        # then
        self.assertTrue(self.decoder.is_blocked())

