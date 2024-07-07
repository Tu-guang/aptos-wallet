from aptos_sdk.account import Account
from mnemonic import Mnemonic
from utils import PublicKeyUtils

for address_index in range(10):
    words = Mnemonic('english').generate()
    # Derivation from BIP44 derivation path
    path = f"m/44'/637'/0'/0'/0'"
    pt = PublicKeyUtils(words, path)
    apt_account = Account.load_key(pt.private_key.hex())
    print(f"{words} {apt_account.address()} 0x{pt.private_key.hex()}")
    with open("wallet.txt",'a',encoding='utf-8') as f:
        f.write(f"{apt_account.address()},0x{pt.private_key.hex()},{words}\n")
