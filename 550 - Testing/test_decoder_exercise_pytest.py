import pytest

from decoder_exercise_solution import *


class TestDecoder:
    def test_by_default_on_standby(self, decoder):
        assert decoder.get_state() == State.standby

    def test_turning_on_and_off(self, decoder):
        decoder.turn_on()
        assert decoder.get_state() == State.on
        decoder.turn_off()
        assert decoder.get_state() == State.standby

    @pytest.mark.parametrize("channel", range(1, 100))
    def test_changing_channels(self, decoder, channel):
        # given
        decoder.turn_on()

        # when
        decoder.set_channel(channel)

        # then
        assert decoder.get_current_channel() == channel

    def test_channel_up_and_down(self, decoder):
        # given
        decoder.turn_on()

        # when
        decoder.set_channel(42)
        decoder.channel_up()

        # then
        assert decoder.get_current_channel() == 43

        # when
        for _ in range(5):
            decoder.channel_down()

        # then
        assert decoder.get_current_channel() == 38

    def test_channel_down_below_0(self, decoder):
        # given
        decoder.turn_on()

        # when
        decoder.set_channel(1)
        with pytest.raises(DecoderException):
            decoder.channel_down()

    @pytest.mark.parametrize("channel", range(-5, 1))
    def test_setting_negative_channel(self, decoder, channel):
        # given
        decoder.turn_on()

        # when
        with pytest.raises(DecoderException):
            decoder.set_channel(channel)

    def test_preserving_channel_channels(self, decoder):
        # given
        decoder.turn_on()
        decoder.set_channel(42)

        # when
        decoder.turn_off()
        decoder.turn_on()

        # then
        assert decoder.get_current_channel() == 42

    def test_default_resolution(self, decoder):
        # given
        decoder.turn_on()

        # expect
        assert decoder.get_resolution() == ResolutionChoice.hd

    def test_changing_resolution(self, decoder):
        # given
        decoder.turn_on()

        # when
        decoder.set_resolution(ResolutionChoice.full_hd)

        # then
        assert decoder.get_resolution() == ResolutionChoice.full_hd

    def test_do_not_operate_on_standby(self, decoder):
        with pytest.raises(DecoderException):
            decoder.set_channel(1)
        with pytest.raises(DecoderException):
            decoder.set_resolution(ResolutionChoice.full_hd)
        with pytest.raises(DecoderException):
            decoder.get_resolution()
        with pytest.raises(DecoderException):
            decoder.channel_up()
        with pytest.raises(DecoderException):
            decoder.channel_down()


