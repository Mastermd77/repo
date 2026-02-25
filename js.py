import json

# 1
json_string = '{"name": "Ali", "age": 19}'
data = json.loads(json_string)
print(data["name"])

# 2
python_dict = {"city": "Almaty", "country": "Kazakhstan"}
json_data = json.dumps(python_dict)
print(json_data)

# 3
with open("data.json", "w") as file:
    json.dump(python_dict, file)

# 4
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

# 5
pretty = json.dumps(python_dict, indent=4)
print(pretty)

# 6
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Dana", "grade": 85}
]

json_students = json.dumps(students)
print(json_students)