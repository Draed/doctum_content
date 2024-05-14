from graphviz import Digraph

def generate_roadmap():
    """Generate a graphical roadmap for becoming a DevOps engineer."""
    dot = Digraph()

    # Define the roadmap steps
    roadmap = [
        "Learn Linux Basics",
        "Learn a Scripting Language (e.g., Bash, Python)",
        "Version Control (e.g., Git)",
        "Continuous Integration (CI) Tools (e.g., Jenkins, Travis CI)",
        "Infrastructure as Code (IaC) (e.g., Terraform, CloudFormation)",
        "Cloud Providers (e.g., AWS, Azure, GCP)",
        "Configuration Management Tools (e.g., Ansible, Puppet)",
        "Containerization (e.g., Docker, Kubernetes)",
        "Monitoring and Logging (e.g., Prometheus, ELK Stack)"
    ]

    # Add nodes (steps) to the graph
    for step in roadmap:
        dot.node(step)

    # Add edges (dependencies) to the graph
    dot.edges([
        ("Learn a Scripting Language (e.g., Bash, Python)", "Learn Linux Basics"),
        ("Version Control (e.g., Git)", "Learn a Scripting Language (e.g., Bash, Python)"),
        ("Continuous Integration (CI) Tools (e.g., Jenkins, Travis CI)", "Version Control (e.g., Git)"),
        ("Infrastructure as Code (IaC) (e.g., Terraform, CloudFormation)", "Continuous Integration (CI) Tools (e.g., Jenkins, Travis CI)"),
        ("Cloud Providers (e.g., AWS, Azure, GCP)", "Infrastructure as Code (IaC) (e.g., Terraform, CloudFormation)"),
        ("Configuration Management Tools (e.g., Ansible, Puppet)", "Infrastructure as Code (IaC) (e.g., Terraform, CloudFormation)"),
        ("Containerization (e.g., Docker, Kubernetes)", "Infrastructure as Code (IaC) (e.g., Terraform, CloudFormation)"),
        ("Monitoring and Logging (e.g., Prometheus, ELK Stack)", "Containerization (e.g., Docker, Kubernetes)")
    ])

    # Render and display the roadmap
    dot.render('roadmap', format='png', cleanup=True)
    dot.view()

def main():
    print("Welcome to the DevOps Engineer Roadmap Generator!")
    print("Generating the graphical roadmap...")

    # Generate the graphical roadmap
    generate_roadmap()

    print("Graphical roadmap generated. Check the generated image.")

if __name__ == "__main__":
    main()
