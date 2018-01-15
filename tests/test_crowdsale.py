from web3.contract import ConciseContract


def test_crowdsale(crowdsale):
    assert isinstance(crowdsale, ConciseContract)
