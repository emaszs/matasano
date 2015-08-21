'''
Created on Aug 21, 2015

@author: EmilisR
'''

import base64
import codecs
import string

class my_ciphers:
    
    
    def hexToBase64(self, hexData):
        """
        Returns a base64 encoded hex string. Base64 has 64 characters, hex has 16.
        Therefore, the resulting string is shorter than input.
        """
        return str(base64.b64encode(codecs.decode(hexData, 'hex')), encoding="UTF-8")
    
    def fixedXOR(self, hex1, hex2):
        """
        XORs two equal-length hex strings with each other.
        """
        xoredStr = ""
        for n1, n2 in zip(hex1, hex2):
            # Convert hex characters to decimal numbers and xor them 
            m1 = int(n1, 16)
            m2 = int(n2, 16)
            xoredStr += hex(m1 ^ m2)[2:]
        return xoredStr
    
    def singleByteCipher(self, code, character):
        """
        Takes hex-encoded string and XORs it against a single character. 
        Since ascii characters are represented by two hex digits (byte), the actual message 
        is only half as long.
        """
        cipherLen = int(len(code) * 0.5)
        cipherString = cipherLen * hex(ord(character)).replace("0x", "")
        return (self.fixedXOR(code, cipherString))
        
    def getCharScore(self, char):
        char = char.lower()
        charScores = {"e" : 12.702, "t" : 9.056, "a" : 8.167,
                     "o" : 7.507, "i" : 6.966, "n" : 6.749,
                     "s" : 6.327, "h" : 6.094, "r" : 5.987,
                     "d" : 4.253, "l" : 4.025, "c" : 2.782,
                     "u" : 2.758, "m" : 2.406, "w" : 2.361,
                     "f" : 2.228, "g" : 2.015, "y" : 1.974,
                     "p" : 1.929, "b" : 1.492, "v" : 0.978,
                     "k" : 0.772, "j" : 0.153, "x" : 0.150,
                     "q" : 0.095, "z" : 0.074, " " : 13.0,
                     "non-alph" : 8.4}
        
        if char.isalpha():
            return charScores[char]
        elif char.isdigit() or char in string.punctuation:
            return charScores["non-alph"]
        elif char == " ":
            return charScores[" "]
        else:
            return 0
        
    def runSbxDecryptTests(self, code):
        for cipher in string.ascii_letters:
            decodedString = self.singleByteCipher(code, cipher)
            print (codecs.decode(decodedString, 'hex'))
#             total = 0
#             for char in decodedString:
#                 
#                 total += self.getCharScore(char)
        
        
