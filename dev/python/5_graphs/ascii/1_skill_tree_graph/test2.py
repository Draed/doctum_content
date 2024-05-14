def generate_skill_tree(skill_tree, indent=0):
    """Generate a simple ASCII representation of the skill tree."""
    for skill, dependencies in skill_tree.items():
        print("  " * indent + "- " + skill)
        generate_skill_tree(dependencies, indent + 1)

def main():
    print("Welcome to the Learning Path Skill Tree Generator!")
    print("Define the skills and their dependencies.")

    # Define the skill tree (skills and their dependencies)
    skill_tree = {
        'Python': {
            'Basic Programming': {
                'Programming Fundamentals': {}
            },
            'Intermediate Programming': {
                'Basic Programming': {},
                'Algorithms': {
                    'Data Structures': {}
                }
            }
        }
        # Add more skills and dependencies as needed
    }

    # Generate the skill tree
    generate_skill_tree(skill_tree)

if __name__ == "__main__":
    main()
