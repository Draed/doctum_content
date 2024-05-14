from graphviz import Digraph

def generate_skill_tree(skill_tree):
    """Generate a learning path skill tree."""
    dot = Digraph()

    # Add nodes (skills) to the graph
    for skill, dependencies in skill_tree.items():
        dot.node(skill)

        # Add dependencies as edges
        for dependency in dependencies:
            dot.edge(dependency, skill)

    # Render and display the skill tree
    dot.render('skill_tree', format='png', cleanup=True)
    dot.view()

def main():
    print("Welcome to the Learning Path Skill Tree Generator!")
    print("Define the skills and their dependencies.")

    # Define the skill tree (skills and their dependencies)
    skill_tree = {
        'Python': ['Basic Programming', 'Intermediate Programming'],
        'Basic Programming': ['Programming Fundamentals'],
        'Intermediate Programming': ['Basic Programming', 'Algorithms'],
        'Algorithms': ['Data Structures'],
        'Data Structures': ['Python']
        # Add more skills and dependencies as needed
    }

    # Generate the skill tree
    generate_skill_tree(skill_tree)

if __name__ == "__main__":
    main()
