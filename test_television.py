import pytest
from television import Television

# Fixture to create a Television instance for each test
@pytest.fixture
def tv():
    return Television()

# Test case for __init__
def test_init(tv):
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == 0
    assert tv._Television__channel == 0

# Test cases for power
def test_power_on(tv):
    tv.power()
    assert tv._Television__status == True

def test_power_off(tv):
    tv.power()
    tv.power()
    assert tv._Television__status == False

# Test cases for mute
def test_mute_on(tv):
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    assert tv._Television__volume == 0

def test_mute_off(tv):
    tv.power()
    tv.mute()
    tv.mute()
    assert tv._Television__muted == False
    assert tv._Television__volume == tv._Television__before_muted

# Test cases for channel_up
def test_channel_up(tv):
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1
    for _ in range(tv._Television__max_channel):
        tv.channel_up()
    assert tv._Television__channel == 0

# Test cases for channel_down
def test_channel_down(tv):
    tv.power()
    for _ in range(tv._Television__max_channel):
        tv.channel_down()
    assert tv._Television__channel == 0
    tv.channel_down()
    assert tv._Television__channel == tv._Television__max_channel

# Test cases for volume_up
def test_volume_up(tv):
    tv.power()
    for _ in range(tv._Television__max_volume):
        tv.volume_up()
    assert tv._Television__volume == tv._Television__max_volume

# Test cases for volume_down
def test_volume_down(tv):
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 0
