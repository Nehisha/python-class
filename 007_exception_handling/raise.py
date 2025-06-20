
divisor = int(input("Enter a number: "))
dividend = 20

if divisor == 0:
    msg = "yesto number nahanana hai"
    raise Exception(msg)

result = divisor / dividend
print(result)
