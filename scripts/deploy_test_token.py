from brownie import StripERC20, WETH, accounts
from scripts.helper_functions import get_account

name = "Strip Token Test"
symbol = "STT"
amount = 100000000 * 10 ** 18


def main():
    account = get_account()

    strip_con = StripERC20.deploy(
        name, symbol, amount, {"from": account}, publish_source=True
    )

    weth_con = WETH.deploy(amount, {"from": account}, publish_source=True)
