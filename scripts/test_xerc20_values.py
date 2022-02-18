from brownie import (
    xERC20,
    ERC20StakingPool,
    ERC721StakingPool,
    StakingPoolFactory,
    StripERC20,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account
import time

xerc20_address = "0xF1169be4956210688c4DF0F6b3759bC09B1Ff9C7"


def print_values():
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    strip = StripERC20.at("0xcB99A4e60dB8D0083179a89EC33d3fB15Be442BD")
    print(f"currentUnlockEndTimestamp {xerc20.currentUnlockEndTimestamp()}")
    print(f"lastRewardTimestamp {xerc20.lastRewardTimestamp()}")
    print(f"lastRewardAmount {xerc20.lastRewardAmount()}")
    print(f"Stake Token {xerc20.stakeToken()}")
    print(f"Duration {xerc20.DURATION()}")
    print(f"xERC20 amount {xerc20.balanceOf(account)/1e18}")
    print(f"Strip amount on my account {strip.balanceOf(account)/1e18}")
    print(f"Strip amount of contract {strip.balanceOf(xerc20.address)/1e18}")
    print(f"Total supply xERC20 {xerc20.totalSupply()/1e18}")
    print(
        f"MULTIPLY BUG {(xerc20.totalSupply()/1e18)*(xerc20.getPricePerFullShare()/1e18)}"
    )
    print("The amount of staked tokens that can be withdrawn by burning 1 xERC20 token")
    print(f"Price per full share {xerc20.getPricePerFullShare()/1e18}")
    STRIP_xERC20 = strip.balanceOf(xerc20.address) / 1e18
    xSTRIP_mul = xerc20.getPricePerFullShare() / 1e18
    xSTRIP_total = xerc20.totalSupply() / 1e18
    sec_year = 31556926
    sec_12_hours = 12 * 60 * 60

    APR_formula = (
        ((STRIP_xERC20 / (xSTRIP_mul * xSTRIP_total)) - 1)
        * (sec_12_hours / (xerc20.currentUnlockEndTimestamp() - time.time()))
        * 100
    )

    print(xerc20.currentUnlockEndTimestamp() - time.time())
    print(f"APR is {APR_formula}")
    print(sec_year / sec_12_hours)


def main():
    print_values()
