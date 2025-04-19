# n = int(input("Enter a decimal number: "))
# s= ""
# while n>0:
#     r = n%8
#     s = str(r)+s
#     n = n//8
# print("Octal code: ",s)

# dec = 0
# i = 0
# while n>0:
#     rem = n%10
#     dec = dec + rem*(8**i)
#     n = n//10
#     i+=1
# print("Decimal number",dec)

# hexa_dec = ""
# while n>0:
#     rem = n%16
#     if rem==10:
#         hexa_dec = "A"+hexa_dec
#     elif rem == 11:
#         hexa_dec = "B"+hexa_dec
#     elif rem == 12:
#         hexa_dec = "C"+hexa_dec
#     elif rem == 13:
#         hexa_dec = "D"+hexa_dec
#     elif rem == 14:
#         hexa_dec = "E"+hexa_dec
#     elif rem == 15:
#         hexa_dec = "F"+hexa_dec
#     else:
#         hexa_dec = str(rem)+hexa_dec
#     n = n//16
# print(hexa_dec)

# n = int(input("Enter a decimal number: "))
# hexa_dec = ""
# hex_chars = "0123456789ABCDEF"
# while n > 0:
#     rem = n % 16
#     hexa_dec = hex_chars[rem] + hexa_dec
#     n = n // 16
# print("Hexadecimal code:", hexa_dec)

hex_num = input("Enter a hexadecimal number: ").upper()
decimal_num = 0
hex_chars = "0123456789ABCDEF"

for digit in hex_num:
    decimal_num = decimal_num * 16 + hex_chars.index(digit)  # Multiply previous value by 16 and add new digit value

print("Decimal number:", decimal_num)
