''' UNILAG AGGREGATOR
5 WAEC CORE COURSES => A1= 4.O , B2= 3.6 , B3= 3.2 , C4= 2.8 , C5= 2.4 , C6=2.0 =(20)
JAMB SCORE = 400/8 =(50)
PUTME SCORE = {30}'''

import os
import time
import sys
print('UNILAG AGGREGATOR')
def g():
	animation = ['Loading |','Loading /','Loading —','Loading \\','Loading |','Loading /', "Loading —", "Loading \\"]*3
	for i in range(len(animation)):
	   	time.sleep(0.075)   
	   	sys.stdout.write('\r'+ animation[i % len(animation)])
g()

WAEC=[]
GRADE=[]
print('\nINPUT YOUR 5 WAEC CORE COURSE GRADES ')
for n in range(5):
	Coursegrade=str.upper(input(''))
	if Coursegrade == 'A1':
		Grade=4.0
	elif Coursegrade == 'B2':
		Grade=3.6
	elif Coursegrade == 'B3':
		Grade=3.2
	elif Coursegrade == 'C4':
		Grade=2.8
	elif Coursegrade == 'C5':
		Grade=2.4
	elif Coursegrade == 'C6':
		Grade=2.0
	else:
		print('YOU DID NOT ENTER A CORRECT COURSE GRADE')
	grade=Grade
	WAEC.append(Coursegrade)
	GRADE.append(grade)	


JAMB=int(input('INPUT YOUR JAMB SCORE : '))
PUTME=int(input('INPUT YOUR PUTME SCORE : '))

jamb_conv=float((JAMB/8))
sum_grade=float((sum(GRADE)))

print('YOUR WAEC CORE COURSE GRADES ARE : ')
print(WAEC)
print('[WAEC GRADES] = ',GRADE)
print('YOUR JAMB SCORE IS {}/400 \n[JAMB GRADE] = {}/50'.format(JAMB,jamb_conv))
print('YOUR PUTME SCORE IS {}/30\n[PUTME GRADE] = {}/30'.format(PUTME,PUTME))

UNILAG_AGGREGATOR=float((sum_grade) + (jamb_conv) + (PUTME))

print('YOUR UNILAG AGGREGATE SCORE IS {} + {} + {} = {}'.format(sum_grade,jamb_conv,PUTME,UNILAG_AGGREGATOR))
