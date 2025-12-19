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
    animals_info += '<li class="cards__item">'

    if "name" in animal:
        animals_info += f' <div class="card__title"> {animal['name']}</div>\n'

    animals_info += '<p class="card__text">'
    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        animals_info += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        animals_info += f"<strong>Locations:</strong> {animal['locations'][0]}<br/>\n"

    if "type" in characteristics:
        animals_info += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"

    animals_info += '</p>\n'
    animals_info += '</li>\n'

    print()

# Replace placeholder in template
final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Write final HTMl file

with open("animals.html", "w") as file:
    file.write(final_html)