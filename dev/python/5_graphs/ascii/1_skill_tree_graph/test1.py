def generate_skill_tree(skill_tree, indent=''):
    """Generate a visual ASCII representation of the skill tree."""
    for index, (skill, dependencies) in enumerate(skill_tree.items(), start=1):
        print(indent + ('└─' if index == len(skill_tree) else '├─') + skill)
        if dependencies:
            generate_skill_tree(dependencies, indent + ('   ' if index == len(skill_tree) else '│  '))

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
