pragma solidity ^0.4.2;

import './PlayerSpecificAddresses.sol';

contract Player is PlayerSpecificAddresses {

    mapping (address => bytes32) currentTrack;

    function stream(bytes32 keccakTrackHash) external returns (bytes32) {
        address listener = msg.sender;
        bytes32 trackHash = data.convertKeccackHashToIPFSHash(keccakTrackHash);
        mp3.transferFromUserToTrack(listener, trackHash, constants.tokensPerStream());
        data.incrementPlayCount(trackHash);
        currentTrack[listener] = trackHash;
    }

    function getCurrentTrack(address listener) view external returns (bytes1, bytes1, bytes32) {
        bytes32 trackHash = currentTrack[listener];
        var (hashFunction, size) = data.getIpfsHashMetadata(trackHash);
        return (hashFunction, size, trackHash);
    }

}

