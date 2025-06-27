my_info = dict(name="Nehisha Hirachan", age="19", grade="A+", email="")
print(my_info["name"])
print(my_info["age"])
print(my_info["grade"])

my_info = my_info.get("email", "No email provided")
print(my_info)
