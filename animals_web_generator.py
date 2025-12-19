import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

# Load animal data
animals_data = load_data('animals_data.json')

# Read HTML template
with open("animals_template.html", "r") as file:
    template_html = file.read()

# Animal info string
animals_info = ""

for animal in animals_data:
    if "name" in animal:
        animals_info += f"Name: {animal['name']}\n"

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        animals_info += f"Diet: {characteristics['diet']}\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        animals_info += f"Locations: {animal['locations'][0]}\n"

    if "type" in characteristics:
        animals_info += f"Type: {characteristics['type']}\n"

    print()

# Replace placeholder in template
final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Write final HTMl file

with open("animals.html", "w") as file:
    file.write(final_html)