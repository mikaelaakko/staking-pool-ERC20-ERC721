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


xerc20_address = "0x02571De0598eFeBB7A6f53e03CBC239d04629CbA"  # CONFIRMED
erc20pool_address = "0x385dE61Fcedd62f8F573a84e46F2ee7c9F79916e"  # CONFIRMED
distributor_address = "0x1E6C27E91Ec9FCF3353896B855dC377E419Ad4c6"  # CONFIRMED


def set_distributor_xerc20():
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    set_distributor = xerc20.setRewardDistributor(
        distributor_address, True, {"from": account}
    )
    set_distributor.wait(1)
    print(f"Reward distributor {xerc20.isRewardDistributor(distributor_address)}")


def set_distributor_erc20pool():
    account = get_account()
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    set_distributor = erc20pool.setRewardDistributor(
        distributor_address, True, {"from": account}
    )
    set_distributor.wait(1)
    print(f"Reward distributor {erc20pool.isRewardDistributor(distributor_address)}")


def main():
    set_distributor_xerc20()
    set_distributor_erc20pool()
