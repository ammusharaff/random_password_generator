import random

lower_case_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_case_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_charcs = "!@#$%^&*_-|\?/"

generate = lower_case_alpha + upper_case_alpha + numbers + special_charcs
print('enter the length of the password you need .......!!!!!')
length_of_password = int(input())

password = "".join(random.sample(generate , length_of_password))

print("your generated password is :")
print(password)