pragma solidity ^0.4.2;

import '../ownership/Ownable.sol';
import '../mp3/MP3.sol';
import '../constants/Constants.sol';

contract CrowdsaleSpecificAddresses is Ownable {

	address public constantsAddress;
    address public mp3Address;
    MP3 mp3;
    Constants constants;

    function setMP3Address(address addr) onlyOwner public {
        mp3Address = addr;
        mp3 = MP3(mp3Address);
    }

    function setConstantsAddress(address addr) onlyOwner public {
        constantsAddress = addr;
        constants = Constants(constantsAddress);
    }

}



