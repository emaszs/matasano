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
#             print (code)
            decodedString = self.singleByteCipher(code, cipher)
            print ("Decrypted string:", decodedString, "Cipher:", cipher)
#             print (decodedString)
            decodedString = codecs.decode(decodedString, "hex")
#             print (decodedString)
            decodedString = codecs.decode(decodedString, "UTF-8", "replace")
#             print (decodedString)
#             print ("Decoded string: ", decodedString)
            total = 0
            for char in decodedString:
                total += self.getCharScore(char)
#             print (total, cipher)
            if total > bestTotal:
                bestTotal = total
                bestChar = cipher
                
                
        hexDecodedString = self.singleByteCipher(code, bestChar)
        print ("Hex decoded string:", hexDecodedString)  
        hexActualString = codecs.decode(hexDecodedString, 'hex')  
        print ("Actual hex string:", hexActualString)    
        bestDecodedString = codecs.decode(hexActualString, 'UTF-8', "replace")
        print ("Resulting string:", bestDecodedString, "Score:", bestTotal, "Chars: ")
        return (bestTotal, bestChar, bestDecodedString)
        
    def sbxDecryptMultipleLines(self, inputFile):
        bestScore = 0
        bestString = ""
        bestChar = ""
        bestResult = []
        with open(inputFile, 'r') as f:
            for line in f:
#                 print ("Running decrypt on", line)
                result = self.runSbxDecryptTests(line)
                score = result[0]
                if score > bestScore:
                    bestScore = score
                    bestString = result[2]
                    bestChar = result[1]
                    bestResult = result
            
        print (bestResult)
        