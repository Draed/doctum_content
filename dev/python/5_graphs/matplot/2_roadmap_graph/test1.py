def generate_roadmap(steps):
    """Generate a roadmap with visual bullet points based on the steps provided."""
    print("Roadmap:")
    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")

def main():
    print("Welcome to the Roadmap Generator!")
    print("Define the steps for your roadmap.")

    steps = []
    while True:
        step = input("Enter a step (or type 'done' when finished): ")
        if step.lower() == 'done':
            break
        steps.append(step)

    generate_roadmap(steps)

if __name__ == "__main__":
    main()