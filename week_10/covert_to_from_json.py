import json

def j(anything):
    # Convert a Python object to a JSON string
    return json.dumps(anything)

# Convert a JSON string to a Python dictionary
student_record = open("week_10/student_record.json", "r").read()
parsed_record = json.loads(student_record)
print(parsed_record)

# Convert a Python dictionary to a JSON string
student_record = {
    "name": "John Doe",
    "year": 1,
    "college": "Dawson"
}
json_string = json.dumps(student_record)
print(json_string)
#list in a tuple
print(json.dumps(("apple", [1,2,3])))
print(json.dumps(23.5))
print(json.dumps(True))
print(json.dumps(None))