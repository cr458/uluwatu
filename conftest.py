import pytest
from web3 import Web3
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from eth_utils import (
	to_checksum_address,
)
from ethereum import (
    tester,
)


@pytest.fixture(scope="module")
def web3():
    provider = EthereumTesterProvider()
    return Web3(provider)


@pytest.fixture(scope="module")
def user0(web3):
    return tester.keys[0], to_checksum_address(tester.accounts[0])


@pytest.fixture(scope="module")
def user1(web3):
    return tester.keys[1], to_checksum_address(tester.accounts[1])


@pytest.fixture(scope="module")
def user2(web3):
    return tester.keys[2], to_checksum_address(tester.accounts[2])
