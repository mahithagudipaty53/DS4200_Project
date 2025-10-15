import pandas as pd
import altair as alt
import webbrowser
import os

# Load dataset
df = pd.read_csv('shopping_behavior_updated.csv')

# Build stacked bar chart
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Season:N', title='Season', sort=['Winter', 'Spring', 'Summer', 'Fall']),
    y=alt.Y('count():Q', title='Number of Purchases'),
    color=alt.Color('Category:N', title='Product Category'),
    tooltip=['Season', 'Category', 'count()']
).properties(
    title='Popularity of Product Categories Across Seasons',
    width=700,
    height=400
)

# Save chart as HTML in current directory
output_file = 'seasonal_category_popularity.html'
chart.save(output_file)
print(f"Saved chart to: {os.path.abspath(output_file)}")

# Open the chart in your default web browser
webbrowser.open('file://' + os.path.abspath(output_file))

