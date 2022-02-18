from brownie import StakingPoolFactory, StripERC20, ERC20StakingPool, Contract
from scripts.helper_functions import get_account

stakingpoolfactory_address = "0x79299aE10e63d79DcDd2eE21920320977156E254"
strip_address = "0xcB99A4e60dB8D0083179a89EC33d3fB15Be442BD"
LP_address = "0x4F69581d1048ecDc5F537B13ECE7fE6aDF6DB602"
duration_threehours = 3 * 60 * 60
rewards = 25000000000 * 10 ** 18
erc20pool_address = "0xf75e5658F16D95f2938329D09535A5514F7FBaf7"


def deploy_erc20pool(duration):
    account = get_account()
    strip = StripERC20.at(strip_address)
    # LP_token = UniswapV2ERC20.at(LP_address)
    contract = Contract(LP_address)
    factory = StakingPoolFactory[-1]

    staking_factory_contract = factory.createERC20StakingPool(
        strip, contract, duration, {"from": account}
    )

    print(f"Pool created!")


def set_distributor():
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    set_distributor = erc20pool.setRewardDistributor(account, True, {"from": account})
    set_distributor.wait(1)
    print(f"Reward distributor {erc20pool.isRewardDistributor(account)}")


def approve():
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    strip = StripERC20.at(strip_address)

    balance_strip = strip.balanceOf(account)
    print(f"Balance of strip {balance_strip}")
    approve_tx = strip.approve(erc20pool.address, balance_strip, {"from": account})
    approve_tx.wait(1)
    print(f"Allowance amount {strip.allowance(account, erc20pool.address)}")


def stake_xerc20(amount):
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)

    stake_tokens = erc20pool.stake(amount * 10 ** 18, {"from": account})
    stake_tokens.wait(1)


def distribute_reward(amount):
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    strip = StripERC20.at(strip_address)

    transfer_tx = strip.transfer(erc20pool.address, amount, {"from": account})
    transfer_tx.wait(1)
    print(f"Strip amount {strip.balanceOf(erc20pool.address)}")

    set_rewards = erc20pool.notifyRewardAmount(amount, {"from": account})
    set_rewards.wait(1)
    print("New reward period started!")


def main():
    # deploy_erc20pool(duration_threehours)
    # set_distributor()
    # approve()
    stake_xerc20(15000000000)
    distribute_reward(rewards)


"""rewardPerTokenStored +
            FullMath.mulDiv(
                (lastTimeRewardApplicable_ - lastUpdateTime) * PRECISION,
                rewardRate_,
                totalSupply_
            );"""

# rewardPerTokenStored += (time_left * rewardRate)/totalsupply

# value-of-LP-token = amount-of-STRIP-in-LP-pool * 2 / LP-token-supply

# APR = (rewardRate * sec_in_year / value-of-LP-token) * 100%

# rewardRate = rewardPerTokenStored * totalsupply/ time_left

# APR = ((rewardPerTokenStored * totalsupply_staked * sec_in_year) / (value-of-LP-token * time_left)) * 100%
