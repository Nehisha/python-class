try:
    num = int(input("Enter your number: "))
    result = 10 / num
    print(f"The result is: {result}")
except ValueError:
    print("Ramro num deu")
except ZeroDivisionError:
    print("0 le divide hunna")
except Exception as e:
    print(f"yesto error ayo: {e}")
finally:
    print("Error ayo")
