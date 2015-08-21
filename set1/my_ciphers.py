'''
Created on Aug 21, 2015

@author: EmilisR
'''

import base64
import codecs

class my_ciphers:

    def hexToBase64(self, hexData):
        return str(base64.b64encode(codecs.decode(hexData, 'hex')), encoding="UTF-8")
    
    def fixedXOR(self, hex1, hex2):
        xoredStr = ""
        for n1, n2 in zip(hex1, hex2):
            m1 = int(n1, 16)
            m2 = int(n2, 16)
            print(hex(m1 ^ m2))
            xoredStr += hex(m1 ^ m2)[2:]
        return xoredStr

