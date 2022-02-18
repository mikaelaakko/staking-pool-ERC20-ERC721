from brownie import StakingPoolFactory, StripERC20, xERC20
from scripts.helper_functions import get_account

stakingpoolfactory_address = "0x79299aE10e63d79DcDd2eE21920320977156E254"
strip_address = "0xcB99A4e60dB8D0083179a89EC33d3fB15Be442BD"
xERC20_address = "0xF1169be4956210688c4DF0F6b3759bC09B1Ff9C7"
duration_threehours = 3 * 60 * 60
rewards = 5000000000 * 10 ** 18


def deploy_xerc20(name, symbol, decimals, duration):
    account = get_account()
    strip = StripERC20.at(strip_address)
    factory = StakingPoolFactory.at(stakingpoolfactory_address)

    staking_factory_contract = factory.createXERC20(
        name, symbol, decimals, strip, duration, {"from": account}
    )

    print(f"Pool created!")


def set_distributor():
    account = get_account()
    xerc20 = xERC20.at(xERC20_address)
    set_distributor = xerc20.setRewardDistributor(account, True, {"from": account})
    set_distributor.wait(1)
    print(f"Reward distributor {xerc20.isRewardDistributor(account)}")


def approve():
    account = get_account()
    xerc20 = xERC20.at(xERC20_address)
    strip = StripERC20.at(strip_address)

    balance_strip = strip.balanceOf(account)
    print(f"Balance of strip {balance_strip}")
    approve_tx = strip.approve(xerc20.address, balance_strip, {"from": account})
    approve_tx.wait(1)
    print(f"Allowance amount {strip.allowance(account, xerc20.address)}")


def stake_xerc20(amount):
    account = get_account()
    xerc20 = xERC20.at(xERC20_address)

    stake_tokens = xerc20.stake(amount, {"from": account})
    stake_tokens.wait(1)


def distribute_reward(amount):
    account = get_account()
    xerc20 = xERC20.at(xERC20_address)
    strip = StripERC20.at(strip_address)
    print(f"Allowance amount {strip.allowance(account, xerc20.address)}")

    set_rewards = xerc20.distributeReward(amount, {"from": account})
    set_rewards.wait(1)
    print("New reward period started!")


def withdraw_xerc20(amount):
    account = get_account()
    xerc20 = xERC20.at(xERC20_address)
    withdraw_tokens = xerc20.withdraw(amount, {"from": account})
    withdraw_tokens.wait(1)


def main():
    name = "Strip staking pool"
    symbol = "xSTRIP"
    name_hex = "0x785374726970207374616b696e6720706f6f6c"
    symbol_hex = "0x785354524950"
    # deploy_xerc20(name_hex, symbol_hex, 18, duration_threehours)
    # set_distributor()
    # approve()
    # withdraw_xerc20(15000000000 * 10 ** 18)
    stake_xerc20(15000000000 * 10 ** 18)
    distribute_reward(rewards)
