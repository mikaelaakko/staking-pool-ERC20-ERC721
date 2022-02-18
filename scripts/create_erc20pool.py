from brownie import (
    StakingPoolFactory,
    StripERC20,
    WETH,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account

strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"
weth_address = "0x55eD4d3A07e41D446A4213C797057b10A53B9e79"
week_seconds = 604800


def deploy_factory(duration):
    account = get_account()
    strip = StripERC20.at(strip_address)
    weth = WETH.at(weth_address)
    factory = StakingPoolFactory[-1]

    staking_factory_contract = factory.createERC20StakingPool(
        strip, weth, duration, {"from": account}
    )

    print(f"Pool {staking_factory_contract} created!")


def main():
    name = "Strip staking pool"
    symbol = "SSP"
    name_hex = "0x5374726970207374616B696E6720706F6F6C"
    symbol_hex = "0x535350"
    deploy_factory(week_seconds)
