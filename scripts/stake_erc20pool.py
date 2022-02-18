from brownie import (
    xERC20,
    WETH,
    ERC20StakingPool,
    ERC721StakingPool,
    StakingPoolFactory,
    StripERC20,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account

erc20_staking_pool = ""
strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"
week_seconds = 604800
weth_address = "0x55eD4d3A07e41D446A4213C797057b10A53B9e79"


def stake_erc20(amount):
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20_staking_pool)
    weth = WETH.at(weth_address)

    balance_weth = weth.balanceOf(account)
    print(f"Balance of weth {balance_weth}")
    approve_tx = weth.approve(erc20pool.address, balance_weth, {"from": account})
    approve_tx.wait(1)
    print(f"Allowance amount {weth.allowance(account, erc20pool.address)}")

    stake_tokens = erc20pool.stake(amount * 10 ** 18, {"from": account})
    stake_tokens.wait(1)


def withdraw_erc20(amount):
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20_staking_pool)
    withdraw_tokens = erc20pool.withdraw(amount * 10 ** 18, {"from": account})
    withdraw_tokens.wait(1)


def main():
    stake_erc20(500000)
    withdraw_erc20(1000000)
