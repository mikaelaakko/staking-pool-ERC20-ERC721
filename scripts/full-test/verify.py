from brownie import xERC20, ERC20StakingPool
from scripts.helper_functions import get_account

xERC20_address = "0xF1169be4956210688c4DF0F6b3759bC09B1Ff9C7"
erc20pool_address = "0xf75e5658F16D95f2938329D09535A5514F7FBaf7"


def verify():
    erc20pool = ERC20StakingPool.at(erc20pool_address)
    print(erc20pool.bytecode)
    ERC20StakingPool.publish_source(erc20pool)
    xerc20 = xERC20.at(xERC20_address)
    print(xerc20.bytecode)
    xERC20.publish_source(xerc20)


def main():
    verify()
