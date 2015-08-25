'''
Created on Aug 21, 2015

@author: EmilisR
'''

import base64
import string
import codecs

class my_ciphers:
    
    
    def hexToBase64(self, hexData):
        """
        Returns a base64 encoded hex string. Base64 has 64 characters, hex has 16.
        Therefore, the resulting string is shorter than input.
        """
        return str(base64.b64encode(bytes.fromhex(hexData)), encoding="UTF-8")
    
    def fixedXOR(self, hex1, hex2):
        """
        XORs two equal-length hex strings with each other.
        """
        xoredStr = ""
        for n1, n2 in zip(hex1, hex2):
            # Convert hex characters to decimal ints and XOR them 
            m1 = int(n1, 16)
            m2 = int(n2, 16)
            xoredStr += hex(m1 ^ m2)[2:]
        return xoredStr
    
    def singleByteCipher(self, code, character):
        """
        Takes hex-encoded string and XORs it against a single character. 
        Since ascii characters are represented by two hex digits (a byte), the actual message 
        is only half as long.
        """
        cipherLen = int(len(code) * 0.5)
        cipherString = cipherLen * hex(ord(character)).replace("0x", "")
        return (self.fixedXOR(code, cipherString))
        
    def getCharScore(self, char):
        char = char.lower()
        charScores = {   "e" : 12.70, "t" : 9.056, "a" : 8.167,
                         "o" : 7.507, "i" : 6.966, "n" : 6.749,
                         "s" : 6.327, "h" : 6.094, "r" : 5.987,
                         "d" : 4.253, "l" : 4.025, "c" : 2.782,
                         "u" : 2.758, "m" : 2.406, "w" : 2.361,
                         "f" : 2.228, "g" : 2.015, "y" : 1.974,
                         "p" : 1.929, "b" : 1.492, "v" : 0.978,
                         "k" : 0.772, "j" : 0.153, "x" : 0.150,
                         "q" : 0.095, "z" : 0.074, " " : 13.0,
                         "non-alph" : 8.4}
        
        if char.isalpha() and char in charScores:
            return charScores[char]
        elif char == " ":
            return charScores[" "]
        else:
            return 0
        
    def runSbxDecryptTests(self, code):
        """
        Tries all the letters of the alphabet on a hex sbx-ed string. Calculates score total.
        Returns string that scored the most (is most likely to be english), score and character.
        """
        bestTotal = 0
        bestChar = ""
        for cipher in string.ascii_letters + string.digits + string.punctuation:
            # XOR string with a single byte ascii character
            decodedString = self.singleByteCipher(code, cipher)
            # Get bytes from the resulting hex string
            decodedString = bytes.fromhex(decodedString)
            # Get UTF-8 from bytes
            decodedString = decodedString.decode("UTF-8", "replace")

            total = 0
            for char in decodedString:
                total += self.getCharScore(char)
            if total > bestTotal:
                bestTotal = total
                bestChar = cipher
                
        hexDecodedString = self.singleByteCipher(code, bestChar)
        byteHexString = bytes.fromhex(hexDecodedString) 
        bestDecodedUtfString = byteHexString.decode("UTF-8", "replace")
        return (bestTotal, bestChar, bestDecodedUtfString)
        
    def sbxDecryptMultipleLines(self, inputFile):
        bestScore = 0
        bestResult = []
        with open(inputFile, 'r') as f:
            for line in f:
                result = self.runSbxDecryptTests(line)
                score = result[0]
                if score > bestScore:
                    bestScore = score
                    bestResult = result
            
        return bestResult
        
    def utf8ToHex(self, data):
        res = ""
        for char in data:
            res += hex(ord(char)).replace("0x", "")
        return res
        
    def repeatingKeyXor(self, inputData, key): 
        # TODO
        keyLen = len(key)
        
        res = ""
        for i in range(len(inputData)):
            keyChar = key[i % keyLen]
            dataChar = inputData[i]
            hexKeyChar = hex(ord(keyChar)).replace("0x", "").zfill(2)
            hexDataChar = hex(ord(dataChar)).replace("0x", "").zfill(2)
            res += self.fixedXOR(hexKeyChar, hexDataChar)
        return res
    
    def calculateHammingDist(self, input1, input2):
        binInput1 = bytes(input1, 'ascii')
        binInput2 = bytes(input2, 'ascii')
        # XOR all bytes. Set bits then indicate the places where the strings are different bite-wise.
        xorBytes = bytes([b1^b2 for (b1,b2) in zip(binInput1, binInput2)])
        # For each byte, count the 1st bit 8 times and then shift it right.
        return sum( (xorBytes[j] >> i) & 1 for i in range(8) for j in range(len(xorBytes)))
        print (xorBytes.count(b'1'))
        print (xorBytes.count(1))
            