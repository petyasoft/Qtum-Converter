from hdwallet import HDWallet
from hdwallet.cryptocurrencies.qtum import Qtum as QTUM
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.derivations import BIP44Derivation

class Qtum():
    def __init__(self, mnemonic : str = ''):
        self.mnemonic = mnemonic
    
    def get_address(self, count : int = 0):
        wallet = HDWallet(cryptocurrency=QTUM)
        wallet.from_mnemonic(
            mnemonic=BIP39Mnemonic(
                mnemonic=self.mnemonic
            )
        ).from_derivation(derivation=BIP44Derivation(coin_type=2301,account=count))
        
        
        return {"mnemonic" : self.mnemonic,
                "address" : wallet.address(),
                "private" : wallet.wif()}
        
        
with open("mnemonics.txt",'r',encoding='utf-8') as file:
    mnemonics = [mnemo.strip() for mnemo in file.readlines()]
    
for mnemonic in mnemonics:
    COUNT_DERIVATION_PATH = 1
    for count in range(COUNT_DERIVATION_PATH):
        try:
            keys = Qtum(mnemonic=mnemonic)
            info = keys.get_address(count)
            with open("address.txt",'a') as file:
                file.write(info["address"]+'\n')
            with open("private.txt",'a') as file:
                file.write(info["private"]+'\n')
            with open("alldata.txt",'a') as file:
                file.write(info["mnemonic"]+' '+info["private"]+' '+info["address"]+'\n')
        except:
            continue
