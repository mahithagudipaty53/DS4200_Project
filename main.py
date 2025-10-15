print("hello")


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_behavior_updated.csv")

df['Incentive_Type'] = df.apply(
    lambda r: 'Used Both' if r['Discount Applied'] == 'Yes' and r['Promo Code Used'] == 'Yes'
    else 'Used Discount Only' if r['Discount Applied'] == 'Yes'
    else 'Used Promo Only' if r['Promo Code Used'] == 'Yes'
    else 'Used Neither', axis=1
)


categories = ['Used Both', 'Used Discount Only', 'Used Promo Only', 'Used Neither']

data = [df.loc[df['Incentive_Type'] == cat, 'Purchase Amount (USD)plt.figure(figsize=(8,6))

plt.figure(figsize=(8,6))
plt.boxplot(data, labels=categories, patch_artist=True)
plt.title('Effect of Incentives on Purchase Amount', fontsize=14, weight='bold')
plt.xlabel('Incentive Type', fontsize=12)
plt.ylabel('Purchase Amount (USD)', fontsize=12)
plt.show()