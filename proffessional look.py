import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Create sample dataframe (since your 'df' wasn't defined)
np.random.seed(42)
data = {
    'age': np.random.randint(20, 65, 100),
    'income': np.random.normal(50000, 15000, 100).astype(int),
    'education_num': np.random.randint(8, 20, 100),
    'hours_per_week': np.random.randint(20, 60, 100)
}
df = pd.DataFrame(data)

# Set style
sns.set_theme(style="whitegrid")

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Create the plot
scatter = ax.scatter(
    x='age', 
    y='income', 
    c='education_num', 
    cmap='viridis',
    alpha=0.7,
    data=df,
    s=df['hours_per_week']/2,  # Size by hours
    edgecolor='w',  # Add white borders
    linewidth=0.5
)

# Customizations
ax.set_title('Income by Age and Education', pad=20, fontsize=14)
ax.set_xlabel('Age (years)', labelpad=10)
ax.set_ylabel('Annual Income ($)', labelpad=10)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Education Level', rotation=270, labelpad=15)

plt.tight_layout()
plt.show()
