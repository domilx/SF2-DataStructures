import json

input_file = open("week_10/student_record.json", "r")
data = json.load(input_file)
input_file.close()
print(data)
print(type(data))

#serializing
output_file = open("week_10/butterflies.json", "w")
d = {
    "painted lady": 1,
    "monarch": 2,
    "red admiral": 3
}
json.dump(d, output_file)
output_file.close()