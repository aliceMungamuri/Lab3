'''
Author: Alice Mungamuri
KUID: 3117704
Date:03/05/2024
Lab: lab#3
Last modified: 03/05/2024
Purpose: Outbreak!
'''
print('OUTBREAK!')
day = int(input('What day do you want a sick count for?: '))
days = [1,4,64]
numPpl = 0 
if day >0:
  for i in (0,day-4):
    nextDay = days[i]+days[i+1]+days[i+2]
    days.append(nextDay)
    i+=1
  print(days[day-1])


    
elif day <= 0:
  print('Invalid Day')
