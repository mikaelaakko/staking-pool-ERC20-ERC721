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

strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"
week_seconds = 604800

xerc20_address = "0x234F258AC1c25E18B073c78EF8e0317beF7fBa71"


def stake_xerc20(amount):
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    strip = StripERC20.at(strip_address)

    balance_strip = strip.balanceOf(account)
    print(f"Balance of strip {balance_strip}")
    approve_tx = strip.approve(xerc20.address, balance_strip, {"from": account})
    approve_tx.wait(1)
    print(f"Allowance amount {strip.allowance(account, xerc20.address)}")

    stake_tokens = xerc20.stake(amount * 10 ** 18, {"from": account})
    stake_tokens.wait(1)


def withdraw_xerc20(amount):
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    withdraw_tokens = xerc20.withdraw(amount * 10 ** 18, {"from": account})
    withdraw_tokens.wait(1)


def main():
    stake_xerc20(1000)
    # withdraw_xerc20(500000)
