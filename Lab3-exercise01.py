'''
Author: Alice Mungamuri
KUID: 3117704
Date:02/15/2024
Lab: lab#3
Last modified: 02/01/2024
Purpose: Sequence Search
'''
word = input('Enter a string: ')
case = input('Do you want a case-sensitive match? (y/n): ')
sqnc = input('Enter a sequence to count: ')
num = 0
if case.upper() == 'Y':
  num = word.count(sqnc)
elif case.upper() == 'N':
  word1 = word.upper()
  sqnc1 = sqnc.upper()
  num = word1.count(sqnc1)

  

print('In the string '+ word+' the sequence "'+ sqnc+'" occurs '+ str(num) +' times')
