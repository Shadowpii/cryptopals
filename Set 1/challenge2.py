"Fixed XOR"

xor1 = "1c0111001f010100061a024b53535009181c"
xor2 = "686974207468652062756c6c277320657965"

result = "746865206b696420646f6e277420706c6179"

def fixed_xor(a,b):
    val = hex(int(a,16)^int(b,16))
    return val[2:].replace("0x","")

x = fixed_xor(xor1,xor2)

if(x == result):
    print("Success!")
else:
    print("Failure!")