curyear=2021
year=int(input("enter a year"))
while curyear<year:
	if (curyear%400==0)or(curyear%100!=0)and(curyear%4==0):
		print(curyear,",")
	curyear=curyear+1
