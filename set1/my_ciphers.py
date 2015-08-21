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

c = my_ciphers()
a = c.fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print (codecs.decode(a, "hex"))
b = c.hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
print (codecs.decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "hex"))