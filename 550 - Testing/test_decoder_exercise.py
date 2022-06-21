import unittest

from decoder_exercise_solution import *


class TestDecoder(unittest.TestCase):
    decoder = None

    def setUp(self) -> None:
        self.decoder = Decoder()

    def test_by_default_on_standby(self):
        self.assertEqual(self.decoder.get_state(), State.standby)

    def test_turning_on_and_off(self):
        self.decoder.turn_on()
        self.assertEqual(self.decoder.get_state(), State.on)
        self.decoder.turn_off()
        self.assertEqual(self.decoder.get_state(), State.standby)

    def test_changing_channels(self):
        # given
        self.decoder.turn_on()

        # when
        self.decoder.set_channel(42)

        # then
        self.assertEqual(self.decoder.get_current_channel(), 42)

    def test_channel_up_and_down(self):
        # given
        self.decoder.turn_on()

        for channel in range(1, 100):
            with self.subTest():
                # when
                self.decoder.set_channel(42)
                self.decoder.channel_up()

                # then
                self.assertEqual(self.decoder.get_current_channel(), 43)

                # when
                for _ in range(5):
                    self.decoder.channel_down()

                # then
                self.assertEqual(self.decoder.get_current_channel(), 38)

    def test_channel_down_below_0(self):
        # given
        self.decoder.turn_on()

        # when
        self.decoder.set_channel(1)
        with self.assertRaises(DecoderException):
            self.decoder.channel_down()

    def test_setting_negative_channel(self):
        # given
        self.decoder.turn_on()

        # when
        for channel in range(-5, 1):
            with self.subTest():
                with self.assertRaises(DecoderException):
                    self.decoder.set_channel(channel)

    def test_preserving_channel_channels(self):
        # given
        self.decoder.turn_on()
        self.decoder.set_channel(42)

        # when
        self.decoder.turn_off()
        self.decoder.turn_on()

        # then
        self.assertEqual(self.decoder.get_current_channel(), 42)

    def test_default_resolution(self):
        # given
        self.decoder.turn_on()

        # expect
        self.assertEqual(self.decoder.get_resolution(), ResolutionChoice.hd)

    def test_changing_resolution(self):
        # given
        self.decoder.turn_on()

        # when
        self.decoder.set_resolution(ResolutionChoice.full_hd)

        # then
        self.assertEqual(self.decoder.get_resolution(), ResolutionChoice.full_hd)

    def test_do_not_operate_on_standby(self):
        with self.assertRaises(DecoderException):
            self.decoder.set_channel(1)
        with self.assertRaises(DecoderException):
            self.decoder.set_resolution(ResolutionChoice.full_hd)
        with self.assertRaises(DecoderException):
            self.decoder.get_resolution()
        with self.assertRaises(DecoderException):
            self.decoder.channel_up()
        with self.assertRaises(DecoderException):
            self.decoder.channel_down()


