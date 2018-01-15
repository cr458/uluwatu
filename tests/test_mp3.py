from web3.contract import ConciseContract


def test_mp3(mp3):
    assert isinstance(mp3, ConciseContract)
