def generate_skill_tree(skill_tree, indent=''):
    """Generate a visual ASCII representation of the skill tree."""
    num_skills = len(skill_tree)
    for index, (skill, dependencies) in enumerate(skill_tree.items(), start=1):
        branch_indent = indent + ('│  ' if index < num_skills else '   ')
        print(indent + ('├─' if index < num_skills else '└─') + skill)
        if dependencies:
            generate_skill_tree(dependencies, branch_indent)

def main():
    print("Welcome to the Learning Path Skill Tree Generator!")
    print("Define the skills and their dependencies.")

    # Define the skill tree (skills and their dependencies)
    skill_tree = {
        'Programming': {
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
            },
            'Java': {
                'Basic Java': {
                    'Object-Oriented Programming': {}
                },
                'Intermediate Java': {
                    'Basic Java': {},
                    'Advanced Java': {
                        'Java EE': {}
                    }
                }
            }
        }
        # Add more skills and dependencies as needed
    }

    # Generate the skill tree
    generate_skill_tree(skill_tree)

if __name__ == "__main__":
    main()
