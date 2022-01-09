current_year=2021
year=int(input("enter a year"))
while current_year<year:
	if (current_year%400==0)or(current_year%100!=0)and(current_year%4==0):
		print(current_year,",")
	current_year=current_year+1
