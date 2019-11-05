from decimal import Decimal, ROUND_HALF_UP

def st10(income):
	print('Your tax bracket is: 10%')
	return (income*.10)

def st12(income):
	print('Your tax bracket is: 12%')
	return (970.00 + ((income-9700.00 )*.12))

def st22(income):
	print('Your tax bracket is: 22%')
	return (4543.00 + ((income-39475.00)*.22))

def st24(income):
	print('Your tax bracket is: 24%')
	return (14382.00+((income-84200.00)*.24))

def st32(income):
	print('Your tax bracket is: 32%')
	return (32748.00+ ((income-160725.00)*.32))

def st35(income):
	print('Your tax bracket is: 35%')
	return (46628.00 + ((income-204100.00)*.35))

def st37(income):
	print('Your tax bracket is: 37%')
	return (153798.00 + ((income-510300.00)*.37))
###########################################
def ht10(income):
	print('Your tax bracket is: 10%')
	return (income*.10)

def ht12(income):
	print('Your tax bracket is: 12%')
	return (1385.00 + ((income-13850.00)*.12))

def ht22(income):
	print('Your tax bracket is: 22%')
	return (6065.00 + ((income-52850.00)*.22))

def ht24(income):
	print('Your tax bracket is: 24%')
	return (12962.00+((income-84200.00)*.24))

def ht32(income):
	print('Your tax bracket is: 32%')
	return (31322.00+ ((income-160700.00)*.32))

def ht35(income):
	print('Your tax bracket is: 35%')
	return (45210.00 + ((income-204100.00)*.35))

def ht37(income):
	print('Your tax bracket is: 37%')
	return (152380.00 + ((income-510300.00)*.37))
##################################################
def mjt10(income):
	print('Your tax bracket is: 10%')
	return (income*.10)

def mjt12(income):
	print('Your tax bracket is: 12%')
	return (1940.00 + ((income-19400.00)*.12))

def mjt22(income):
	print('Your tax bracket is: 22%')
	return (9086.00 + ((income-78950.00)*.22))

def mjt24(income):
	print('Your tax bracket is: 24%')
	return (28765.00+((income-168400.00)*.24))

def mjt32(income):
	print('Your tax bracket is: 32%')
	return (65497.00+ ((income-321450.00)*.32))

def mjt35(income):
	print('Your tax bracket is: 35%')
	return (93257.00 + ((income-408200.00)*.35))

def mjt37(income):
	print('Your tax bracket is: 37%')
	return (164709.00 + ((income-612350.00)*.37))
###################################################
def mst10(income):
	print('Your tax bracket is: 10%')
	return (income*.10)

def mst12(income):
	print('Your tax bracket is: 12%')
	return (970.00 + ((income-9700.00)*.12))

def mst22(income):
	print('Your tax bracket is: 22%')
	return (4543.00 + ((income-39475.00)*.22))

def mst24(income):
	print('Your tax bracket is: 24%')
	return (14382.50+((income-84200.00)*.24))

def mst32(income):
	print('Your tax bracket is: 32%')
	return (32748.50+ ((income-160725.00)*.32))

def mst35(income):
	print('Your tax bracket is: 35%')
	return (46628.50 + ((income-204100.00)*.35))

def mst37(income):
	print('Your tax bracket is: 37%')
	return (82354.75 + ((income-510300.00)*.37))
	############################################

c = 'c'
deductions = 12000.00

while c.lower() == 'c':
	filing = input("Please enter you filing status:\nS - Single, Unmarried\nH - Head of Household\nMJ - Married Filing Jointly\nMS - Married Filing Separately\n")
	filing = filing.lower()
	income = int(input('Please enter you income\n'))
	pre_deducted_income = income
	pre_tax_contributions = int(input("What are your IRA contributions?\n"))
	deductions += pre_tax_contributions
	income = income - deductions
	if income < 0:
		income = 0

	tax = 0.00

	if filing == 's':
		if income < 9701.00:
			tax = st10(income)
		elif income < 39476.00:
			tax = st12(income)
		elif income < 84201.00:
			tax = st22(income)
		elif income < 169726.00:
			tax = st24(income)
		elif income < 204101.00:
			tax = st32(income)
		elif income < 510300.00:
			tax = st35(income)
		elif income > 510300.00:
			tax = st37(income)
	if filing == 'h':
		if income < 13851.00:
			tax = ht10(income)
		elif income < 52851.00:
			tax = ht12(income)
		elif income < 84201.00:
			tax = ht22(income)
		elif income < 160701.00:
			tax = ht24(income)
		elif income < 204101.00:
			tax = ht32(income)
		elif income < 510300.00:
			tax = ht35(income)
		elif income > 510300.00:
			tax = ht37(income)
	if filing == 'mj':
		if income < 19401.00:
			tax = mjt10(income)
		elif income < 78951.00:
			tax = mjt12(income)
		elif income < 168401.00:
			tax = mjt22(income)
		elif income < 321451.00:
			tax = mjt24(income)
		elif income < 408201.00:
			tax = mjt32(income)
		elif income < 612351.00:
			tax = mjt35(income)
		elif income > 612350.00:
			tax = mjt37(income)
	if filing == 'ms':
		if income < 9701.00:
			tax = mst10(income)
		elif income < 39476.00:
			tax = mst12(income)
		elif income < 84201.00:
			tax = mst22(income)
		elif income < 160726.00:
			tax = mst24(income)
		elif income < 204101.00:
			tax = mst32(income)
		elif income < 510301.00:
			tax = mst35(income)
		elif income > 510300.00:
			tax = mst37(income)
	effectiveTax = (100.00)*(tax)/(pre_deducted_income)
	print('Your effective tax rate is: {:.4f}%'.format(effectiveTax))
	print('Your tax is: ${:.2f}'.format(tax))
	dispInc = (pre_deducted_income-tax)
	print('Your income after tax is: ${:.2f}'.format(dispInc))
	c = input("Enter 'c' to restart\n")
	filing = 'n'