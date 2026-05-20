import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create assets directory
if not os.path.exists('assets'):
    os.makedirs('assets')

# Load data
df = pd.read_csv('customer_churn_data.csv')
df['SignupDate'] = pd.to_datetime(df['SignupDate'])
df['ChurnDate'] = pd.to_datetime(df['ChurnDate'])

# 1. Overall Churn Rate
churn_rate = df['IsChurned'].mean() * 100
print(f"Overall Churn Rate: {churn_rate:.2f}%")

# 2. Churn Reasons Distribution
churned_df = df[df['IsChurned'] == 1]
plt.figure(figsize=(10, 6))
sns.countplot(data=churned_df, y='ChurnReason', order=churned_df['ChurnReason'].value_counts().index, palette='Reds_r')
plt.title('Primary Reasons for Customer Churn')
plt.tight_layout()
plt.savefig('assets/churn_reasons.png')
plt.close()

# 3. Churn by Subscription Plan
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Plan', y='IsChurned', palette='viridis')
plt.title('Churn Rate by Subscription Plan')
plt.ylabel('Churn Rate')
plt.tight_layout()
plt.savefig('assets/churn_by_plan.png')
plt.close()

# 4. Retention Drivers: Support Tickets vs Churn
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='IsChurned', y='SupportTickets', palette='Set2')
plt.title('Support Tickets vs Customer Churn')
plt.xticks([0, 1], ['Active', 'Churned'])
plt.tight_layout()
plt.savefig('assets/support_vs_churn.png')
plt.close()

# 5. Customer Lifetime Trends: Cohort Analysis (Monthly Signup)
df['CohortMonth'] = df['SignupDate'].dt.to_period('M')
cohort_counts = df.groupby('CohortMonth')['CustomerID'].nunique().reset_index()
cohort_counts['CohortMonth'] = cohort_counts['CohortMonth'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(data=cohort_counts, x='CohortMonth', y='CustomerID', marker='o')
plt.title('New Customer Signups by Cohort Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('assets/cohort_signups.png')
plt.close()

# 6. Customer Lifetime Value (CLV) Analysis
clv_by_plan = df.groupby('Plan')['TotalCharges'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=clv_by_plan, x='Plan', y='TotalCharges', palette='magma')
plt.title('Average Customer Lifetime Value (CLV) by Plan')
plt.ylabel('Avg Total Revenue per Customer')
plt.tight_layout()
plt.savefig('assets/clv_by_plan.png')
plt.close()

print("Churn analysis complete. Visualizations saved in 'TASK2/assets/' folder.")

# Summary statistics
summary_stats = {
    'Total Customers': len(df),
    'Churned Customers': df['IsChurned'].sum(),
    'Churn Rate': f"{churn_rate:.2f}%",
    'Avg Tenure (Months)': df['TenureMonths'].mean(),
    'Avg CLV': df['TotalCharges'].mean(),
    'Top Churn Reason': churned_df['ChurnReason'].value_counts().idxmax()
}

print("\n--- Churn & Retention Summary ---")
for key, value in summary_stats.items():
    print(f"{key}: {value}")
