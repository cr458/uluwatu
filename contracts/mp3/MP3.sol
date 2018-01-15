pragma solidity ^0.4.16;


import './TrackTransferableToken.sol';


/**
 * @title MP3
 * @dev Highest level of Token Contract
 */
contract MP3 is TrackTransferableToken {

    string public name;
    string public symbol;
    uint8 public decimals;
    event Transfer(address _from, address _to, uint256 _value);

    function MP3() public {
        name = 'MP3';
        symbol = 'MP3';
        decimals = 0;
    }
    
}