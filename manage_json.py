import json

# Assuming the JSON content is stored in a file named 'data.json'
with open('./ControlEval/second_order_unstable_data.json', 'r') as file:
    data = json.load(file)

# Process each dictionary in the list to update keys and remove unnecessary ones
for item in data:

    # Add the new key `scenario` with value `fat`
    item["scenario"] = "other"

# Write the updated data back to the JSON file or print to verify
with open('./ControlEval/second_order_unstable_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully.")
