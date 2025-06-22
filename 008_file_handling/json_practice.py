# 1.Write a Python program to convert JSON data to Python object.
import json

json_ko_data = '{"name": "Nehisha","age": "19","city" : "pokhara"}'
python_ko_obj = json.loads(json_ko_data)

print(python_ko_obj)
print(type(python_ko_obj))

# 2.Write a Python program to convert Python object to JSON data.

python_ko_obj = {
    "name": "Nehisha",
    "age": "19",
    "city": "pokhara"
}
json_data = json.dumps(python_ko_obj)

print(json_data)
print(type(json_data))

# 3.Write a Python program to convert Python objects into JSON strings. Print all the values.

python_obj = {"name": "Nehisha", "age": "19", "city": "pokhara"}
json_data_ho = json.dumps(python_obj)
print(json_data_ho)

json_dict = json.loads(json_data_ho)
for value in json_dict.values():
    print(value)
