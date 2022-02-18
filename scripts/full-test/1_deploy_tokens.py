from brownie import StripERC20, WETH, accounts
from scripts.helper_functions import get_account

name = "Strip Coin"
symbol = "SC"
amount_strip = 500000000000 * 10 ** 18
amount_weth = 5000 * 10 ** 18


def main():
    account = get_account()

    strip_con = StripERC20.deploy(
        name, symbol, amount_strip, {"from": account}, publish_source=True
    )

    weth_con = WETH.deploy(amount_weth, {"from": account}, publish_source=True)
