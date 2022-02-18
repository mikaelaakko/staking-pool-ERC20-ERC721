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

three_months_seconds = 7776000


def deploy_factory(name, symbol, decimals, duration):
    account = get_account()
    strip = Contract(strip_address)
    factory = StakingPoolFactory.at(stakingpoolfactory_address)

    staking_factory_contract = factory.createXERC20(
        name, symbol, decimals, strip, duration, {"from": account}
    )

    print(f"Pool {staking_factory_contract.events} created!")


def main():
    name = "xSTRIP Staking Pool"
    symbol = "xSTRIP"
    name_hex = "0x785354524950205374616b696e6720506f6f6c"
    symbol_hex = "0x785354524950"
    deploy_factory(name_hex, symbol_hex, 18, three_months_seconds)
