import codecs

# This string needs to be converted from HEX to Base64
string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

decoded = codecs.decode(string, 'hex')
base64 = codecs.encode(decoded, 'base64').decode()

print(base64)