import numpy as np
import matplotlib.pyplot as plt

# Define the skills and their performance values
skills = ['Speed', 'Memory', 'Concentration']
performance_values = {
    'Speed': 75,
    'Memory': 60,
    'Concentration': 80
}

# Convert performance values to percentages
max_score = 100
performance_percentages = {skill: value / max_score * 100 for skill, value in performance_values.items()}

# Plot the radar chart
# Adapted from: https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html
labels = np.array(list(performance_percentages.keys()))
values = np.array(list(performance_percentages.values()))
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

values = np.concatenate((values,[values[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.25)
ax.plot(angles, values, color='skyblue', linewidth=3)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_title('Skill Mapping')

plt.show()
