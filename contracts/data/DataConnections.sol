pragma solidity ^0.4.2;


import '../ownership/Ownable.sol';
import '../mp3/MP3.sol';
import '../constants/Constants.sol';


contract DataConnections is Ownable {
    address public constantsAddress;
    address public playerAddress;
    address public mp3Address;
    MP3 mp3;
    Constants public constants;


    function setPlayerAddress(address addr) public {
        playerAddress = addr;
    }
    

    function setMP3Address(address addr) public {
        mp3Address = addr;
        mp3 = MP3(mp3Address);
    }


    function setConstantsAddress(address addr) public {
        constantsAddress = addr;
        constants = Constants(constantsAddress);
    }
}

