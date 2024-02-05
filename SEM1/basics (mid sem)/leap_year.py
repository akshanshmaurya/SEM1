start_year=int(input("enter the start year:"))
end_year=int(input("enter the end year:"))
leap_years=[]
for year in range(start_year,end_year+1):
    if(year%4==0 and year%100!=0) or (year%400==0):
        leap_years.append(year)
if len(leap_years)>0:
    print(f"the leap years between{start_year} and{end_year}are:")
    print(leap_years)
else:
    print(f"there are no leap years between {start_year} and {end_year}")