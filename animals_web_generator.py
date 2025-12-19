import json

def load_data(file_path):
  """ Loads a JSON file and return its content. """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal):
    """Serializes a single animal object into an HTML list item."""
    # Animal info string
    output = ""
    output += '<li class="cards__item">'

    # Title.
    if "name" in animal:
        output += f' <div class="card__title"> {animal["name"]}</div>\n'

    output += '<p class="card__text">'

    characteristics = animal.get("characteristics", {})

    # Diet.
    if "diet" in characteristics:
        output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"

    # Locations (first one).
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Locations:</strong> {animal['locations'][0]}<br/>\n"

    # Type.
    if "type" in characteristics:
        output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"

    output += '</p>\n'
    output += '</li>\n'

    return output


def main():
    """Main program flow."""

    # Load animal data
    animals_data = load_data('animals_data.json')

    # Read HTML template
    with open("animals_template.html", "r") as file:
        template_html = file.read()

    animals_info = ""

    for animal in animals_data:
        animals_info += serialize_animal(animal)

    # Replace placeholder in template
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write final HTMl file
    with open("animals.html", "w") as file:
        file.write(final_html)

if __name__ == "__main__":
    main()