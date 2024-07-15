#Decimal to roman from scratch
#By Amer

from time import sleep

def dec_to_rom(n):
	debug=0
	if len(str(n))==1:
		if n==0:
			return ''
		elif n >= 1 and n <= 3:
			return 'I'*n
		elif n == 4:
			return 'IV'
		elif n == 5:
			return 'V'
		elif n >= 6 and n <= 8:
			return ('V'+(n-5)*'I')
		elif n == 9:
			return 'IX'
		elif n == 10:
			return 'X'
			
		
		
	if len(str(n)) == 2:
		n10 = (n - n%10) / 10
		
		if debug == 1:
			print('n is '+str(n))
			print('n10 is '+str(int(n10)))
		
		elif n10 in (1,2,3):
			return 'X'*int(n10) + dec_to_rom(n%10)
			
		elif n10 == 4:
			return 'XL' + dec_to_rom(n%10)
			
		elif n == 50:
			return 'L'
			
		elif n10 == 5:
			return 'L' + dec_to_rom(n%10)
			
		elif n10 in (6,7,8):
			return ('L'+(int(n10)-5)*'X') + dec_to_rom(n%10)

		elif n10 == 9:
			return 'XC' + dec_to_rom(n%10)
			
	if len(str(n)) == 3:
		n100 = (n - n%100) / 100
		n10 = (n - n%10) / 10
		
		if n == 100:
			return 'C'
			
		elif n100 in (1,2,3):
			return 'C'*int(n100) + dec_to_rom(n%100)

		elif n100 == 4:
			return 'CD' + dec_to_rom(n%100)

		elif n == 500:
			return 'D'
			
		elif n100 == 5:
			return 'D' + dec_to_rom(n%100)
			
		elif n100 in (6,7,8):
			return 'D' + (int(n100)-5)*'C' + dec_to_rom(n%100)
			
		elif n100 == 9:
			return 'CM' + dec_to_rom(n%100)
			
	if len(str(n)) == 4:
		n1000 = (n - n%1000) / 1000
		n100 = (n - n%100) / 100
		n10 = (n - n%10) / 10
		
		if n == 1000:
			return 'M'
test=1

def dots():
	for i in range(2):
		sleep(0)
		print('.',end=' ',flush=True)
	sleep(0)
	print('.',flush=True)

if test == 1:	
	print('Generating Roman numerals',end='')
	dots()
	print()
		
	for i in range(1,1001):
		if i%100 == 0:
			print(str(i) + ': '+str(dec_to_rom(i)))
			print('')
			print('')
			sleep(0.1)
			
		elif i%10 == 0 and i%100 != 0:
			print(str(i) + ': '+str(dec_to_rom(i)))
			print('')
			sleep(0.1)
			
		else:
			print(str(i) + ': '+str(dec_to_rom(i)))
			sleep(0.1)
