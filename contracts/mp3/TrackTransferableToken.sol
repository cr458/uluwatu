pragma solidity ^0.4.2;


import './MintableToken.sol';


/**
 * @title MP3
 * @dev Adds ERC20-esque functionality for tranferring tokens from users to tracks
 */
contract TrackTransferableToken is MintableToken {

    mapping (bytes32 => uint256) trackBalances;
    event TransferFromUserToTrack(address _from, bytes32 _to, uint256 _value);

    /**
    * @dev Get the balance of the specified track hash.
    * @param trackHash The track hash to query the the balance of.
    */
    function trackBalanceOf(bytes32 trackHash) view public returns (uint256) {
        return trackBalances[trackHash];
    }

    /**
    * @dev Transfer token to a specified track hash
    * @param _from The address to transfer from.
    * @param _to The track hash to transfer to.
    * @param _value The amount to be transferred.
    */
    function transferFromUserToTrack(address _from, bytes32 _to, uint256 _value) external returns (bool) {
        require(_value <= balances[_from]); // User has funds
        require(_value <= allowed[_from][msg.sender]); // User has allowed Player to withdraw funds

        // SafeMath.sub will throw if there is not enough balance.
        balances[_from] = balances[_from].sub(_value);
        trackBalances[_to] = trackBalances[_to].add(_value);
        allowed[_from][msg.sender] = allowed[_from][msg.sender].sub(_value);
        TransferFromUserToTrack(msg.sender, _to, _value);
        return true;
    }


}