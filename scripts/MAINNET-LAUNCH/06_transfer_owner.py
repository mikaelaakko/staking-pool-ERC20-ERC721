from brownie import (
    xERC20,
    ERC20StakingPool,
    ERC721StakingPool,
    StakingPoolFactory,
    Contract,
    accounts,
    network,
    config,
)
from scripts.helper_functions import get_account


multi_sig = "0x194fE3F75D69ea398486E1e48105a83367663B28"

xerc20_proxy_address = "0x97a9ebD15ec0C8528616e38Ea14FF14aE57Ae651"
erc20stake_proxy_address = "0x7eb0eC6237A941c097506f70Be340D268B7826F4"
erc721stake_proxy_address = "0x82239f14D4Afe635C911Cd725a3bBc3702E658f4"
stakingpoolfactory_address = "0x41f6cF6650E2Eb5BFAE22C1015a3e187BE928aA7"

xerc20_address = "0x02571De0598eFeBB7A6f53e03CBC239d04629CbA"  # CONFIRMED
erc20pool_address = "0x385dE61Fcedd62f8F573a84e46F2ee7c9F79916e"  # CONFIRMED


def transfer_ownership():
    account = get_account()
    # factory = StakingPoolFactory.at(stakingpoolfactory_address)
    xerc20_proxy = xERC20.at(xerc20_proxy_address)
    erc20stake_proxy = ERC20StakingPool.at(erc20stake_proxy_address)
    erc721stake_proxy = ERC721StakingPool.at(erc721stake_proxy_address)

    xerc20 = xERC20.at(xerc20_address)
    erc20stake = ERC20StakingPool.at(erc20pool_address)

    """xerc20_proxy_tx = xerc20_proxy.transferOwnership(multi_sig, {"from": account})
    xerc20_proxy_tx.wait(1)"""

    """erc20stake_proxy_tx = erc20stake_proxy.transferOwnership(
        multi_sig, {"from": account}
    )
    erc20stake_proxy_tx.wait(1)

    erc721stake_proxy_tx = erc721stake_proxy.transferOwnership(
        multi_sig, {"from": account}
    )
    erc721stake_proxy_tx.wait(1)"""

    xerc20_tx = xerc20.transferOwnership(multi_sig, {"from": account})
    xerc20_tx.wait(1)

    erc20stake_tx = erc20stake.transferOwnership(multi_sig, {"from": account})
    erc20stake_tx.wait(1)


def main():
    transfer_ownership()
