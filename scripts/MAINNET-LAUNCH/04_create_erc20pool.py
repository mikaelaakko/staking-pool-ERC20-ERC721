from brownie import (
    xERC20,
    ERC20StakingPool,
    ERC721StakingPool,
    StakingPoolFactory,
    StripERC20,
    Contract,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account


stakingpoolfactory_address = "0x41f6cF6650E2Eb5BFAE22C1015a3e187BE928aA7"
strip_address = "0xE9cB6838902CCF711f16a9EA5A1170F8e9853C02"
LP_address = "0xa759cA7117DEae729B035beE2EDfdA46B279c939"
three_months_seconds = 7776000


def deploy_erc20pool(duration):
    account = get_account()

    strip = Contract(strip_address)
    lp_pool = Contract(LP_address)
    factory = StakingPoolFactory.at(stakingpoolfactory_address)

    staking_factory_contract = factory.createERC20StakingPool(
        strip, lp_pool, duration, {"from": account}
    )

    print(f"Pool {staking_factory_contract.events} created!")


def main():
    deploy_erc20pool(three_months_seconds)
