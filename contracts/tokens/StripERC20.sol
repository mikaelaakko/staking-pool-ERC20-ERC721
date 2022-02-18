// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StripERC20 is ERC20Permit, Ownable {
    using SafeMath for uint256;

    uint256 public requestAmount = 1000000;

    constructor(
        string memory name,
        string memory symbol,
        uint256 amount
    ) ERC20(name, symbol) ERC20Permit(name) {
        //_setupDecimals(decimals);
        _mint(msg.sender, amount);
    }

    mapping(address => uint256) timeLock;

    function requestLohko(address addr) external {
        //require the lockdown period to be over
        require(
            timeLock[addr] < block.timestamp,
            "try again after the lockdown period"
        );

        //mint requested amount of tokens
        _mint(addr, requestAmount);

        //update lockdown for 10 minutes from the last request
        timeLock[addr] = block.timestamp + 10 minutes;
    }

    function setRequestAmount(uint256 _requestAmount) external onlyOwner {
        requestAmount = _requestAmount;
    }
}
