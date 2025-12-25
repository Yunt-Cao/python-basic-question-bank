result=0
for num in range(1,100):
    if num % 2 == 1:
        result+=num**2
    else:
        result-=num**2
print(result)