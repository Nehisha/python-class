# def multiply(*args):
#     product = 1
#     for item in args:
#         product = product * item
#     return product


# result = multiply(2, 3, 4, 5)
# print(result)


def greet(**kwargs):
    firstname = kwargs["First Name: "]
    middlename = kwargs.get("Middle Name: ", None)
    lastname = kwargs["First Name: "]

    print(firstname)
    print(middlename)
    print(lastname)

result = greet(firstname="Nehisha", Middlename="", lastname="Hirachan")
