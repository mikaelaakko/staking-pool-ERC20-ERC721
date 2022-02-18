from brownie import (
    ERC20StakingPool,
    StripERC20,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account


def print_values():
    account = get_account()
    erc20pool = ERC20StakingPool.at("0xd2524Fbc2205D6803c8597aad62b1866E21dB909")
    strip = StripERC20.at("0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478")
    print(f"Reward period finish {erc20pool.periodFinish()}")
    print(f"Stake Token {erc20pool.stakeToken()}")
    print(f"Reward Token {erc20pool.rewardToken()}")
    print(f"Duration {erc20pool.DURATION()}")
    print(f"WETH amount {erc20pool.balanceOf(account)}")
    print(f"Strip amount {strip.balanceOf(account)}")
    print(f"Total supply WETH {erc20pool.totalSupply()}")
    print("The amount of reward tokens each staked token has earned so far")
    print(f"Reward per token {erc20pool.rewardPerToken()/1e18}")
    print(f"Reward earned by account {erc20pool.earned(account)/1e18}")


def main():
    print_values()
