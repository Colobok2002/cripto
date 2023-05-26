import operator 


def number_perestanovka(key, seq):
    
    new_key = ""
    for digit in seq:
        new_key += key[int(digit)]

    return new_key


def S1S2(number):
    
    table_S1 = {'00':{'00': '01', '01':'11', '10':'00', '11':'11'},
                '01':{'00': '00', '01':'10', '10':'10', '11':'01'},
                '10':{'00': '11', '01':'01', '10':'01', '11':'11'},
                '11':{'00': '10', '01':'00', '10':'11', '11':'01'}}
    
    table_S2 = {'00': {'00': '01', '01': '10', '10': '11', '11': '10'},
                '01': {'00': '01', '01': '00', '10': '00', '11': '01'},
                '10': {'00': '10', '01': '01', '10': '01', '11': '00'},
                '11': {'00': '11', '01': '11', '10': '00', '11': '11'}}

    
    L = number[0:4]
    R = number[4:8]
    L_row = L[0] + L[3]
    L_column = L[1:3]
    R_row = R[0] + R[3]
    R_column = R[1:3]
    out_number = table_S1[L_column][L_row] + table_S2[R_column][R_row]

    return number_perestanovka(out_number, "1320")

def F_func(message, key):
    
    number = number_perestanovka(message, "3012") + number_perestanovka(message, "1230")
    number = "".join(str(operator.xor(int(number_bit), int(key_bit)))
                     for number_bit, key_bit in zip(number, key))
    number = S1S2(number)
    
    return number


K = bin(1003)[2:] 
X = bin(159)[2:]


new_K = number_perestanovka(K, "2416390875")

new_K = new_K[1:5] + new_K[0] + new_K[6:10] + new_K[5] 
K1 = number_perestanovka(new_K, "52637498")

new_K = new_K[2:5] + new_K[0:2] + new_K[7:10] + new_K[5:7]
K2 = number_perestanovka(new_K, "52637498") 



new_X = number_perestanovka(X, "15203746")
new_XL = new_X[:4]
new_XR = new_X[4:8]


XR = F_func(new_XR, K1) 



new_XL = "".join(str(operator.xor(int(XR_bit), int(new_XL_bit)))
                 for XR_bit, new_XL_bit in zip(XR, new_XL))

new_X = new_XR + new_XL
new_XL = new_X[:4]
new_XR = new_X[4:8]



XR = F_func(new_XR, K2)

new_XL = "".join(str(operator.xor(int(XR_bit),
                    int(new_XL_bit)))
                    for XR_bit, new_XL_bit in zip(XR, new_XL))
new_X = new_XL + new_XR

print(new_X)
final_X = number_perestanovka(new_X, "30246175")

print(final_X)

print(int(final_X, 2))
