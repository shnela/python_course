from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/decoder.feature')


@given('decoder is turned on')
def turn_decoder_on(decoder):
    decoder.turn_on()


# @given('decoder is turned on check')
# def turn_decoder_on(decoder):
#     decoder.get_state() == Sta


@when(parsers.parse('the user selects channel {channel}'))
def set_channel(decoder, channel):
    channel = int(channel)
    decoder.set_channel(channel)


@then(parsers.parse('decoder should be tuned to chanel {channel}'))
def search_results(decoder, channel):
    channel = int(channel)
    assert decoder.get_current_channel() == channel
