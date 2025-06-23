import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # Explicit import recommended

# Load sample data
tips = sns.load_dataset('tips')

# Create plot
sns.set_theme(style="whitegrid")
g = sns.relplot(
    data=tips,
    x="total_bill", y="tip", 
    col="time",  # Creates separate columns for lunch/dinner
    hue="smoker",  # Color encoding
    style="smoker",  # Marker style encoding
    size="size",  # Marker size encoding (party size)
    sizes=(20, 200),  # Explicit size range
    alpha=0.8,  # Slight transparency
    palette="viridis"  # Explicit color palette
)

# Customizations
g.set_axis_labels("Total bill ($)", "Tip ($)")
g.legend.set_title("Smoker")
plt.tight_layout()  # Prevent label overlap

# Optional: Save the figure
# g.savefig('tips_relationship.png', dpi=300, bbox_inches='tight')

plt.show()  # Explicitly show the plot
