import matplotlib.pyplot as plt

def generate_roadmap(steps):
    """Generate a roadmap with visual bullet points based on steps."""
    num_steps = len(steps)

    # Create a scatter plot to represent bullet points
    plt.figure(figsize=(10, 2))
    plt.scatter(steps, [1] * num_steps, marker='o', color='blue', s=500)

    # Annotate each bullet point with step number
    for i, step in enumerate(steps):
        plt.text(step, 1, f"{i+1}", color='white', ha='center', va='center', fontsize=12)

    # Set plot properties
    plt.title('Roadmap')
    plt.xlabel('Steps')
    plt.yticks([])  # Hide y-axis
    plt.grid(False)  # Hide gridlines

    plt.show()

def main():
    print("Welcome to the Roadmap Generator!")
    print("Define the steps of your roadmap.")

    # Input steps from user
    steps = input("Enter the steps (comma-separated): ").split(',')
    steps = [step.strip() for step in steps]

    # Generate the roadmap
    generate_roadmap(steps)

if __name__ == "__main__":
    main()
