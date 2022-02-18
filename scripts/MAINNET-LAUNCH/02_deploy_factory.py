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

xerc20_address = "0x97a9ebD15ec0C8528616e38Ea14FF14aE57Ae651"
erc20stake_address = "0x7eb0eC6237A941c097506f70Be340D268B7826F4"
erc721stake_address = "0x82239f14D4Afe635C911Cd725a3bBc3702E658f4"
# xerc20_address_rinkeby = "0x97a9ebD15ec0C8528616e38Ea14FF14aE57Ae651"
# erc20stake_address_rinkeby = "0x7eb0eC6237A941c097506f70Be340D268B7826F4"
# erc721stake_address_rinkeby = "0x82239f14D4Afe635C911Cd725a3bBc3702E658f4"


def deploy_factory():
    account = get_account()
    xerc20 = xERC20.at(xerc20_address)
    erc20stake = ERC20StakingPool.at(erc20stake_address)
    erc721stake = ERC721StakingPool.at(erc721stake_address)

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
