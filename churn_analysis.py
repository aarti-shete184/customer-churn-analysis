import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('churn_data.csv')

print(df.head())

print("\nMissing Values:\n", df.isnull().sum())

churn_count = df['Churn'].value_counts()
print("\nChurn Distribution:\n", churn_count)

avg_charges = df.groupby('Churn')['MonthlyCharges'].mean()
print("\nAvg Monthly Charges:\n", avg_charges)

churn_count.plot(kind='bar', title='Churn Count')
plt.show()

avg_charges.plot(kind='bar', title='Avg Monthly Charges by Churn')
plt.show()