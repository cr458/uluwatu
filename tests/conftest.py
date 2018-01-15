import pytest
import os
import json
from web3.contract import ConciseContract
from web3.utils.transactions import (
    wait_for_transaction_receipt,
)
from solc import (
    compile_files,
)
from uluwatu import (
    CONTRACTS_DIR,
)


DATA = os.path.join(CONTRACTS_DIR, "data")
PLAYER = os.path.join(CONTRACTS_DIR, "player")
CROWDSALE = os.path.join(CONTRACTS_DIR, "crowdsale")
CONSTANTS = os.path.join(CONTRACTS_DIR, "constants")
MATH = os.path.join(CONTRACTS_DIR, "math")
OWNERSHIP = os.path.join(CONTRACTS_DIR, "ownership")
MP3 = os.path.join(CONTRACTS_DIR, "mp3")


def compile(filepath, contract_name, allow_paths=None):
    compilation = compile_files(
        [filepath],
        allow_paths=allow_paths,
    )
    compilation = compilation[filepath+":"+contract_name]
    abi = json.dumps(compilation['abi'])
    bytecode = compilation['bin']
    bytecode_runtime = compilation['bin-runtime']
    return abi, bytecode, bytecode_runtime


@pytest.fixture(scope="module")
def Constants(web3):
    filepath = os.path.join(CONSTANTS, "Constants.sol")
    contract_name = 'Constants'
    allow_paths = ",".join([MATH, OWNERSHIP])
    abi, code, code_runtime = compile(filepath, contract_name, allow_paths)
    return web3.eth.contract(
        abi=abi,
        bytecode=code,
        bytecode_runtime=code_runtime,
    )


@pytest.fixture(scope="function")
def constants(web3, Constants, user0):
    _priv, owner = user0
    deploy_txn = Constants.deploy()
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn)
    assert deploy_receipt is not None
    _contract = Constants(address=deploy_receipt['contractAddress'])
    concise_contract = ConciseContract(_contract)
    assert owner == concise_contract.owner()
    return concise_contract


@pytest.fixture(scope="module")
def Mp3(web3):
    filepath = os.path.join(MP3, "MP3.sol")
    contract_name = 'MP3'
    allow_paths = ",".join([MATH, OWNERSHIP])
    abi, code, code_runtime = compile(filepath, contract_name, allow_paths)
    return web3.eth.contract(
        abi=abi,
        bytecode=code,
        bytecode_runtime=code_runtime,
    )


@pytest.fixture(scope="function")
def mp3(web3, Mp3, user0):
    _priv, owner = user0
    deploy_txn = Mp3.deploy()
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn)
    assert deploy_receipt is not None
    _contract = Mp3(address=deploy_receipt['contractAddress'])
    concise_contract = ConciseContract(_contract)
    assert owner == concise_contract.owner()
    return concise_contract


@pytest.fixture(scope="module")
def Data(web3):
    filepath = os.path.join(DATA, "Data.sol")
    contract_name = 'Data'
    allow_paths = ",".join([CONSTANTS, MATH, OWNERSHIP, MP3])
    abi, code, code_runtime = compile(filepath, contract_name, allow_paths)
    return web3.eth.contract(
        abi=abi,
        bytecode=code,
        bytecode_runtime=code_runtime,
    )


@pytest.fixture(scope="function")
def data(web3, Data, constants, user0):
    _priv, owner = user0
    deploy_txn = Data.deploy()
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn)
    assert deploy_receipt is not None
    _contract = Data(address=deploy_receipt['contractAddress'])
    concise_contract = ConciseContract(_contract)
    assert owner == concise_contract.owner()
    return concise_contract


@pytest.fixture(scope="module")
def Player(web3):
    filepath = os.path.join(PLAYER, "Player.sol")
    contract_name = 'Player'
    allow_paths = ",".join([CONSTANTS, DATA, MATH, OWNERSHIP, MP3])
    abi, code, code_runtime = compile(filepath, contract_name, allow_paths)
    return web3.eth.contract(
        abi=abi,
        bytecode=code,
        bytecode_runtime=code_runtime,
    )


@pytest.fixture(scope="function")
def player(web3, Player, user0):
    _priv, owner = user0
    deploy_txn = Player.deploy()
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn)
    assert deploy_receipt is not None
    _contract = Player(address=deploy_receipt['contractAddress'])
    concise_contract = ConciseContract(_contract)
    assert owner == concise_contract.owner()
    return concise_contract


@pytest.fixture(scope="module")
def Crowdsale(web3):
    filepath = os.path.join(CROWDSALE, "Crowdsale.sol")
    contract_name = 'Crowdsale'
    allow_paths = ",".join([CONSTANTS, MATH, OWNERSHIP, MP3])
    abi, code, code_runtime = compile(filepath, contract_name, allow_paths)
    return web3.eth.contract(
        abi=abi,
        bytecode=code,
        bytecode_runtime=code_runtime,
    )


@pytest.fixture(scope="function")
def crowdsale(web3, Crowdsale, user0, user2):
    _priv, owner = user0
    _priv, crowdsale_wallet = user2
    deploy_txn = Crowdsale.deploy(args=[crowdsale_wallet])
    deploy_receipt = wait_for_transaction_receipt(web3, deploy_txn)
    assert deploy_receipt is not None
    _contract = Crowdsale(address=deploy_receipt['contractAddress'])
    concise_contract = ConciseContract(_contract)
    assert owner == concise_contract.owner()
    return concise_contract
