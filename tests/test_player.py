from web3.contract import ConciseContract


def test_player(player):
    assert isinstance(player, ConciseContract)
