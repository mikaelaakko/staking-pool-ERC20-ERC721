from brownie import (
    xERC20,
    StripERC20,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account

xerc20_address = "0x785bf8D5e06b55582FdB16788E0697CC1A2Bf8c1"
strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"


def set_distributor():
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    set_distributor = xerc20.setRewardDistributor(account, True, {"from": account})
    set_distributor.wait(1)
    print(f"Reward distributor {xerc20.isRewardDistributor(account)}")


def distribute_reward(amount):
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    strip = StripERC20.at(strip_address)
    print(f"Allowance amount {strip.allowance(account, xerc20.address)}")

    set_rewards = xerc20.distributeReward(amount, {"from": account})
    set_rewards.wait(1)
    print("New reward period started!")


def main():
    set_distributor()
    distribute_reward(500 * 10 ** 18)
