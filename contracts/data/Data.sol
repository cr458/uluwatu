pragma solidity ^0.4.2;

import './DataConnections.sol';

contract Data is DataConnections {
    using SafeMath for uint256;
    

    mapping (bytes32 => bool) uploads;
    mapping (bytes32 => mapping (string => string)) verifiedTrackMetadata;
    mapping (bytes32 => mapping (string => mapping (string => uint256))) valueCounts;
    mapping (bytes32 => bytes1) trackHashFunctions;
    mapping (bytes32 => bytes1) trackHashSizes;
    mapping (bytes32 => bool) captchaHashes;
    mapping (bytes32 => uint256) streams;


    function getVerifiedTrackMetadata(bytes32 trackHash, string _key) 
        view external 
        returns (string) {
        return verifiedTrackMetadata[trackHash][_key];
    }


    function getTrackHashFunction(bytes32 trackHash) 
        view external 
        returns (bytes1) {
        return trackHashFunctions[trackHash];
    }


    function getTrackHashSize(bytes32 trackHash) 
        view external 
        returns (bytes1) {
        return trackHashSizes[trackHash];
    }


    function getValueCount(bytes32 trackHash, string _key, string _value) 
        view external 
        returns (uint256) {
        return valueCounts[trackHash][_key][_value];
    }


    function uploadTrack(
        bytes1 hashFunction, bytes1 size, bytes32 trackHash, 
        string artist, string title)
        external {
        bool firstTime = !uploads[trackHash];
        if (firstTime) {
            verifiedTrackMetadata[trackHash]['artist'] = artist;
            verifiedTrackMetadata[trackHash]['title'] = title;
            trackHashFunctions[trackHash] = hashFunction;
            trackHashSizes[trackHash] = size;
        }
        uploads[trackHash] = true;
    }


    function uploadMetadata(
        bytes32 h, uint8 v, bytes32 r, bytes32 s,
        address _addr, bytes32 trackHash, string _key, string _value, bytes32 captchaHash) 
        public {
        // Verify signer is the service
        address signer = ecrecover(h, v, r, s);
        require(signer == owner);
        // Verfify that the user has supplied values contained in the signature
        bytes memory preamble = "\x19Ethereum Signed Message:\n32";
        bytes32 proof = keccak256(preamble, keccak256(this, _addr, trackHash, _key, _value, captchaHash));
        require(proof == h);
        // Verify that CAPTCHA has not been used before
        require(!captchaHashes[captchaHash])
        captchaHashes[captchaHash] = true;

        uint256 valueCount = valueCounts[trackHash][_key][_value].add(1);
        valueCounts[trackHash][_key][_value] = valueCount;
        uint256 cutoff = constants.verificationRequirement();
        if (valueCount >= cutoff) {
            verifiedTrackMetadata[trackHash][_key] = _value;
        }   
        uint reward = constants.captchaReward();
        mp3.mint(addr, reward);
    }


    function incrementPlayCount(bytes32 trackHash) external {
        streams[trackHash] = streams[trackHash].add(1);
    }


    function getPlayCount(bytes32 trackHash) view external returns (uint) {
        return streams[trackHash];
    }    
}
