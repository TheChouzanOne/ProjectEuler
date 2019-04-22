from time import time
t=time()

days = {
    'jan':31,
    'feb':28,
    'mar':31,
    'apr':30,
    'may':31,
    'jun':30,
    'jul':31,
    'aug':31,
    'sep':30,
    'oct':31,
    'nov':30,
    'dec':31,
}
months = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(" ")

day = 1
ans = 0

for year in range(1900, 2001):
    if(year % 4 == 0 and (year%100!=0 or year%400==0)):
        days['feb'] = 29
    else:
        days['feb'] = 28

    for month in months:
        day += days[month]
        day %= 7
        if(year>1900):
            if day==0:
                ans += 1




print(ans)
print("Time: %s"%(time()-t))