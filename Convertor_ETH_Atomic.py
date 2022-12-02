# Convert Private Key To Ethereum Address and Check Value Balance from Atomic 
# First Install Package's :
# Windows : => pip install lxml hdwallet fake-useragent
# Linux : => pip3 install lxml hdwallet fake-useragent
# Programmer Mmdrza & Official Website: Mmdrza.Com
# //////////////////////////////////////////////////////////////////////////////

from hdwallet import HDWallet
from hdwallet.symbols import ETH as eth
from lxml import html
import requests
from fake_useragent import UserAgent


def GetBal(addr):
    URL_REQ = f"https://ethereum.atomicwallet.io/address/{addr}"
    ua = UserAgent(browsers=['chrome', 'firefox', 'edge', 'safari', 'opera'])
    user_Mmdrza = ua.random
    headers = {"UserAgent": user_Mmdrza}
    SRC_CODE = html.fromstring(requests.get(URL_REQ, headers=headers).content)
    XPATCH = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]'
    TREE_XP = SRC_CODE.xpath(XPATCH)
    BAL_VALUE = str(TREE_XP[0].text_content())
    return BAL_VALUE


found = 0
count = 0
# import all key from text file
filename = "PrivateKey_10M_Nov_2022.txt"
with open(filename, 'r', encoding='utf-8', errors='ignore') as fr:
    for Prikvatekey in fr.readlines():
        Privatekey = Prikvatekey.strip('\n').strip()
        hd: HDWallet = HDWallet(symbol=eth)
        hd.from_private_key(private_key=Privatekey)
        addr = hd.p2pkh_address()
        balance = GetBal(addr)
        count += 1
        iffer = "0 ETH"
        if balance != iffer:
            found += 1
            with open('FoundValue.txt', 'a') as vf:
                vf.write(f"{addr}        Balance: {balance}\n{Privatekey}\n{'=' * 55}\n")
                vf.close()
        else:

            print(f"{count} Address: {addr} # Balance: {balance}\n{Privatekey}\n{'=' * 64}")
