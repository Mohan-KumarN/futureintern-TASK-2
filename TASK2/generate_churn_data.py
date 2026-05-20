import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Parameters
num_customers = 2000
start_date = datetime(2024, 1, 1)

# Subscription Plans
plans = {
    'Basic': 9.99,
    'Standard': 19.99,
    'Premium': 29.99
}

# Churn Reasons
churn_reasons = ['Price too high', 'Found better alternative', 'Poor customer service', 'Technical issues', 'No longer needed', 'Other']

# Generate Customer Data
customer_ids = [f'CUST-{i:04d}' for i in range(1, num_customers + 1)]
signup_dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_customers)]
subscription_plans = np.random.choice(list(plans.keys()), num_customers, p=[0.5, 0.3, 0.2])
monthly_charges = [plans[plan] for plan in subscription_plans]
tenure_months = np.random.randint(1, 24, num_customers)
is_churned = np.random.choice([0, 1], num_customers, p=[0.7, 0.3])

data = []
for i in range(num_customers):
    customer_id = customer_ids[i]
    signup_date = signup_dates[i]
    plan = subscription_plans[i]
    charge = monthly_charges[i]
    tenure = tenure_months[i]
    churned = is_churned[i]
    
    # Calculate end date if churned
    end_date = signup_date + timedelta(days=int(tenure * 30)) if churned else None
    reason = np.random.choice(churn_reasons) if churned else 'N/A'
    
    # Other metrics
    total_charges = round(charge * tenure, 2)
    support_tickets = np.random.randint(0, 10)
    usage_frequency = np.random.choice(['Low', 'Medium', 'High'], p=[0.2, 0.5, 0.3])
    
    data.append([customer_id, signup_date, end_date, plan, charge, tenure, churned, reason, total_charges, support_tickets, usage_frequency])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'CustomerID', 'SignupDate', 'ChurnDate', 'Plan', 'MonthlyCharge', 
    'TenureMonths', 'IsChurned', 'ChurnReason', 'TotalCharges', 
    'SupportTickets', 'UsageFrequency'
])

# Save to CSV
df.to_csv('customer_churn_data.csv', index=False)
print("Customer churn data generated successfully: customer_churn_data.csv")
