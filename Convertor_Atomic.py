from bit import Key
from lxml import html
import requests


def GetBal(addr):
    URL_REQ = f"https://bitcoin.atomicwallet.io/address/{addr}"
    RES_REQ = requests.get(URL_REQ)
    Byte_STR = RES_REQ.content
    SRC_CODE = html.fromstring(Byte_STR)
    XPATCH = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
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
        Private_Key = Key.from_hex(Privatekey)
        # Create Address from Private Key
        addr = Private_Key.address
        balance = GetBal(addr)
        count += 1
        iffer = "0 BTC"
        if balance != iffer:
            found += 1
            with open('FoundValue.txt', 'a') as vf:
                vf.write(f"{addr}        Balance: {balance}\n{PrivateKey}\n{'=' * 55}\n")
                vf.close()
        else:

            print(f"{count} Address: {addr} # Balance: {balance}\n{Privatekey}")
