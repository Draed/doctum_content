from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
import json

def load_roadmap_from_json(file_path):
    """Load roadmap data from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def generate_roadmap_from_json(file_path):
    """Generate an ASCII graphical roadmap for becoming a DevOps engineer from a JSON file."""
    roadmap_data = load_roadmap_from_json(file_path)
    roadmap = Roadmap(1200, 400, colour_theme="BLUEMOUNTAIN")
    roadmap.set_title("My Roadmap")
    roadmap.set_subtitle("Matariki Technologies Inc.")
    # roadmap.set_timeline(mode=TimelineMode.MONTHLY, start="2022-11-14", number_of_items=6)
    roadmap.set_timeline(TimelineMode.MONTHLY, start="2023-01-01", number_of_items=12)

    for node in roadmap_data['nodes']:
        group = roadmap.add_group(node['name'])
        if 'children' in node:
            for child_node in node['children']:
                group.add_task(node['name'], child_node['start'], child_node['end'])
    roadmap.draw()
    roadmap.save("my_roadmap.png")

def main():
    print("Welcome to the DevOps Engineer Roadmap Generator!")
    print("Loading the roadmap from JSON file...\n")

    file_path = 'roadmap.json'  # Path to your JSON file
    generate_roadmap_from_json(file_path)

if __name__ == "__main__":
    main()
