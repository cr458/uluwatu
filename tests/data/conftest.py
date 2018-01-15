import pytest
from web3.utils.transactions import (
    wait_for_transaction_receipt,
)


@pytest.fixture(scope="function")
def connected_data(web3, data, constants, mp3, user0):
    _priv, owner = user0
    # Constants
    txhash = data.setConstantsAddress(constants.address, transact={'from': owner})
    receipt = wait_for_transaction_receipt(web3, txhash)
    assert receipt is not None
    assert data.constantsAddress() == constants.address
    # Mp3
    txhash = data.setMP3Address(mp3.address, transact={'from': owner})
    receipt = wait_for_transaction_receipt(web3, txhash)
    assert receipt is not None
    assert data.constantsAddress() == constants.address
    return data
