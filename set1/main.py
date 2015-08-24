'''
Created on Aug 21, 2015

@author: EmilisR
'''
from set1 import my_ciphers     

c = my_ciphers.my_ciphers()
# a = c.fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
# print (codecs.decode(a, "hex"))
# b = c.hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
# print (codecs.decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "hex"))

code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# a = c.fixedXOR(code, (len(code) * hex(ord("x")) ).replace("0x", ""))

# print ("Code length:", codeLen)
# print ((int(len(code) * 0.5) * hex(ord("x"))).replace("0x", ""))

# c.singleByteCipher(code, "r")
# testCode = codecs.encode(b"Hello world!", "hex")
# print (testCode)     
# testCode = codecs.decode(testCode, "UTF-8")
# print (len(testCode))           
# testCode = c.singleByteCipher(testCode, "a")
# print (testCode)
# testCode = c.singleByteCipher(testCode, "a")
# print (testCode)
# testCode = codecs.decode(testCode, "hex")
# print (testCode)
# print (codecs.decode(testCode, "UTF-8"))
# print (c.runSbxDecryptTests(code))
c.sbxDecryptMultipleLines("60linesOfSbx.txt")