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

erc20pool_address = "0xd2524Fbc2205D6803c8597aad62b1866E21dB909 "
strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"


def set_distributor():
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    set_distributor = erc20pool.setRewardDistributor(account, True, {"from": account})
    set_distributor.wait(1)
    print(f"Reward distributor {erc20pool.isRewardDistributor(account)}")


def distribute_reward(amount):
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    strip = StripERC20.at(strip_address)

    balance_strip = strip.balanceOf(account)
    print(f"Balance of strip {balance_strip}")
    approve_tx = strip.approve(erc20pool.address, balance_strip, {"from": account})
    approve_tx.wait(1)

    print(f"Allowance amount {strip.allowance(account, erc20pool.address)}")

    transfer_tx = strip.transfer(erc20pool.address, amount, {"from": account})
    transfer_tx.wait(1)
    print(f"Strip amount {strip.balanceOf(erc20pool.address)}")

    set_rewards = erc20pool.notifyRewardAmount(amount, {"from": account})
    set_rewards.wait(1)
    print("New reward period started!")


def main():
    set_distributor()
    distribute_reward(20000000 * 10 ** 18)
