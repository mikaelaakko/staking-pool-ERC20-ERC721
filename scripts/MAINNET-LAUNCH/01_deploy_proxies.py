from brownie import (
    xERC20,
    ERC20StakingPool,
    ERC721StakingPool,
    Contract,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account


def deploy_xerc20():
    account = get_account()

    publish_source = True

    xerc20_contract = xERC20.deploy(
        {"from": account},
        publish_source=publish_source,
    )

    print(f"Contract {xerc20_contract.address} deployed!")


def deploy_erc20_staking():
    account = get_account()

    publish_source = True

    erc20staking_contract = ERC20StakingPool.deploy(
        {"from": account},
        publish_source=publish_source,
    )

    print(f"Contract {erc20staking_contract.address} deployed!")


def verify():
    erc20staking_contract = ERC20StakingPool.at(
        "0x7eb0eC6237A941c097506f70Be340D268B7826F4"
    )
    ERC20StakingPool.publish_source(erc20staking_contract)


def deploy_erc721_staking():
    account = get_account()

    publish_source = True
    erc721staking_contract = ERC721StakingPool.deploy(
        {"from": account},
        publish_source=publish_source,
    )

    print(f"Contract {erc721staking_contract.address} deployed!")


def main():
    # deploy_xerc20()
    # deploy_erc20_staking()
    # verify()
    deploy_erc721_staking()
