from eth_utils import (
    keccak,
)
from web3.utils.transactions import (
    wait_for_transaction_receipt,
)


TRACKHASH = b'E\x03/)\x9cvUR\xa1\xc1\xc27\xa3\xd4@\x016T^@\x95\xb4\xc3\t\xdb\xe8}\x1c\xec\r\xdf\xda'  # noqa: E501
ARTIST = 'Black Sabbath'
TITLE = 'Paranoid'


def upload_metadata(
        web3, data, addr,
        trackhash, key, value):
    txhash = data.uploadMetadata(
        trackhash, key, value, addr,
        transact={'from': addr},
    )
    txn_receipt = wait_for_transaction_receipt(web3, txhash)
    assert txn_receipt is not None


def test_value_count(web3, connected_data, user1):
    data = connected_data
    # Expected
    key = 'artist'
    value = ARTIST
    expected_value = 1

    # Actual
    priv, addr = user1
    upload_metadata(
        web3, data, addr,
        TRACKHASH, key, value,
    )
    output_value = data.getValueCount(TRACKHASH, key, value)

    # Test
    assert output_value == expected_value


def test_mint(web3, connected_data, constants, mp3, user1):
    data = connected_data
    # Expected
    key = 'artist'
    expected_value = constants.captchaReward()

    # Actual
    priv, addr = user1
    upload_metadata(
        web3, data, addr,
        TRACKHASH, key, ARTIST,
    )
    output_value = mp3.balanceOf(addr)

    # Test
    assert output_value == expected_value
