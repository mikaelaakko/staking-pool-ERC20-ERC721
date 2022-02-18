from brownie import (
    xERC20,
    ERC20StakingPool,
    ERC721StakingPool,
    StakingPoolFactory,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account


def deploy_factory():
    account = get_account()
    xerc20 = xERC20[-1]
    erc20stake = ERC20StakingPool[-1]
    erc721stake = ERC721StakingPool[-1]

    publish_source = True

    staking_factory_contract = StakingPoolFactory.deploy(
        xerc20,
        erc20stake,
        erc721stake,
        {"from": account},
        publish_source=publish_source,
    )

    print(f"Contract {staking_factory_contract.address} deployed!")


def main():
    deploy_factory()
