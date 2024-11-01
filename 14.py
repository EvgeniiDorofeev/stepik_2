is_leap = lambda x: (x%4==0 and x%100!=0) or x%400==0

print(is_leap.__name__)
print(is_leap(2000))
