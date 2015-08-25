'''
Created on Aug 21, 2015

@author: EmilisR
'''
from set1 import my_ciphers   
import codecs  

c = my_ciphers.my_ciphers()
# Challenge 1
# expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
# b64 = c.hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
# assert b64 == expected
# print (codecs.decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "hex"))
# 
# 
# # Challenge 2
# expected = "746865206b696420646f6e277420706c6179"
# fixed = c.fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
# assert fixed == expected
# print (codecs.decode(fixed, "hex"))
# # print (codecs.decode(a, "hex"))
# # b = c.hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
# # print (codecs.decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "hex"))
# 
# # Challenge 3
# code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
# best = c.runSbxDecryptTests(code)
# assert best[2] == "Cooking MC's like a pound of bacon"
# print (best[2])
# 
# # Challenge 4
# best = c.sbxDecryptMultipleLines("60linesOfSbx.txt")
# assert best[2] == "Now that the party is jumping\n"
# print (best[2])
# 
# # Challenge 5
# expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
# data = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# encrypted = c.repeatingKeyXor(data, "ICE")
# assert expected == encrypted
# print (data)

print (c.calculateHammingDist("this is a test", "wokka wokka!!!"))

