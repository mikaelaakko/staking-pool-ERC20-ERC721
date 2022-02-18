from brownie import (
    StakingPoolFactory,
    StripERC20,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account

strip_address = "0x0Ff63FbbDEe379B4FDA592Ea869188643Ab4c478"
week_seconds = 604800
year_seconds = 31556926


def deploy_factory(name, symbol, decimals, duration):
    account = get_account()

    strip = StripERC20.at(strip_address)
    factory = StakingPoolFactory[-1]

    staking_factory_contract = factory.createXERC20(
        name, symbol, decimals, strip, duration, {"from": account}
    )

    print(f"Pool {staking_factory_contract.address} created!")


def main():
    name = "Strip staking pool v22"
    symbol = "SSPv22"
    name_hex = "0x5374726970207374616B696E6720706F6F6C20763232"
    symbol_hex = "0x535350763232"
    deploy_factory(name_hex, symbol_hex, 18, year_seconds)
