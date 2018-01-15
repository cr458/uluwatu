from web3.utils.transactions import (
    wait_for_transaction_receipt,
)


HASH_FUNCTION = b'\x12'
SIZE = b' '
TRACKHASH = b'E\x03/)\x9cvUR\xa1\xc1\xc27\xa3\xd4@\x016T^@\x95\xb4\xc3\t\xdb\xe8}\x1c\xec\r\xdf\xda'  # noqa: E501
ARTIST = 'Black Sabbath'
TITLE = 'Paranoid'


def upload_track(
        web3, data, addr,
        hash_function, size, trackhash,
        artist, title):
    txhash = data.uploadTrack(
        hash_function, size, trackhash, artist, title,
        transact={'from': addr},
    )
    txn_receipt = wait_for_transaction_receipt(web3, txhash)
    assert txn_receipt is not None


def test_artist(web3, data, user1):
    # Expected
    expected_value = ARTIST

    # Actual
    priv, addr = user1
    upload_track(
        web3, data, addr,
        HASH_FUNCTION, SIZE, TRACKHASH, ARTIST, TITLE,
    )
    output_value = data.getVerifiedTrackMetadata(TRACKHASH, 'artist')

    # Test
    assert output_value == expected_value


def test_title(web3, data, user1):
    # Expected
    expected_value = TITLE

    # Actual
    priv, addr = user1
    upload_track(
        web3, data, addr,
        HASH_FUNCTION, SIZE, TRACKHASH, ARTIST, TITLE,
    )
    output_value = data.getVerifiedTrackMetadata(TRACKHASH, 'title')

    # Test
    assert output_value == expected_value


def test_hash_function(web3, data, user1):
    # Expected
    expected_value = HASH_FUNCTION

    # Actual
    priv, addr = user1
    upload_track(
        web3, data, addr,
        HASH_FUNCTION, SIZE, TRACKHASH, ARTIST, TITLE,
    )
    output_value = data.getTrackHashFunction(TRACKHASH)

    # Test
    assert output_value == expected_value


def test_size(web3, data, user1):
    # Expected
    expected_value = SIZE

    # Actual
    priv, addr = user1
    upload_track(
        web3, data, addr,
        HASH_FUNCTION, SIZE, TRACKHASH, ARTIST, TITLE,
    )
    output_value = data.getTrackHashSize(TRACKHASH)

    # Test
    assert output_value == expected_value
