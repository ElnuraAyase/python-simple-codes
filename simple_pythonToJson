import json

# Function to write data to a JSON file
def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Function to read data from a JSON file
def read_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


# Sample data to write to the JSON file
sample_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Write the sample data to a JSON file
write_to_json(sample_data, 'data.json')

# Read data from the JSON file and display it
read_data = read_from_json('data.json')
print("Data read from JSON file:")
print(read_data)
