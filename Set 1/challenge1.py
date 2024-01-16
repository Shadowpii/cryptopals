# Converting hex to base64
from base64 import b64encode
import binascii 


hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_base64(hex):
    return b64encode(binascii.unhexlify(hex)).decode()

b = hex_to_base64(hex_string)

if(b == base64_string):
    print("Success!")
else:
    print("Failure!")

