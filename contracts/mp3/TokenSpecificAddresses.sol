pragma solidity ^0.4.2;

import '../ownership/Ownable.sol';

contract TokenSpecificAddresses is Ownable {

    address public dataAddress;
    address public crowdsaleAddress;
    
    modifier onlyDataOrCrowdsale() {
        require(msg.sender == dataAddress || msg.sender == crowdsaleAddress);
        _;
    }
    
    function setDataAddress(address addr) onlyOwner public {
        dataAddress = addr;
    }

    function setCrowdsaleAddress(address addr) onlyOwner public {
        crowdsaleAddress = addr;
    }

}

