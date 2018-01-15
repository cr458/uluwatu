pragma solidity ^0.4.2;

import '../math/SafeMath.sol';
import '../ownership/Ownable.sol';

contract Constants is Ownable {
    using SafeMath for uint256;

    uint256 public ethPrice;
    uint256 public centsPerDollar;
    uint256 public weiPerETH;
    uint256 public centsPerStream;
    uint256 public tokensPerStream;
    uint256 public verificationRequirement;
    uint256 public captchaMultiplier;
    uint256 public captchaReward;
    uint256 public weiPerTokens;

    function Constants() public {
        ethPrice = 450;
        centsPerDollar = 100;
        weiPerETH = 1000000000000000000;
        centsPerStream = 10;
        tokensPerStream = 1;
        verificationRequirement = 3;
        captchaMultiplier = 5;
        captchaReward = captchaMultiplier*tokensPerStream;
        weiPerTokens = setWeiPerTokens(ethPrice);
    }
    
    function setVerificationRequirement(uint256 _value) public {
        // verificationRequirement = _value;
    }

    function setCaptchaMultiplier(uint256 _value) onlyOwner public {
        captchaMultiplier = _value;
        captchaReward = captchaMultiplier*tokensPerStream;
    }

    function setTokensPerStream(uint256 _value) onlyOwner public {
        tokensPerStream = _value;
        captchaReward = captchaMultiplier*tokensPerStream;
        setWeiPerTokens(ethPrice);
    }

    function setCentsPerStream(uint256 _value) onlyOwner public {
        centsPerStream = _value;
        setWeiPerTokens(ethPrice);
    }

    function setWeiPerTokens(uint256 _ethPrice) onlyOwner public returns(uint256) {
        ethPrice = _ethPrice;
        uint256 centsPerETH = ethPrice.mul(centsPerDollar);
        uint256 streamsPerETH = centsPerETH.div(centsPerStream);
        uint256 tokensPerETH = tokensPerStream.mul(streamsPerETH);
        weiPerTokens = weiPerETH.div(tokensPerETH);
        return weiPerTokens;
    }

}
