import pandas as pd
from datetime import datetime, timedelta
import random

# Generate a synthetic transactional dataset with timestamps and item quantities
# Setting a seed for reproducibility
random.seed(0)

# Define items and their external utility (profit value)
items = {'a': 5, 'b': 3, 'c': 2, 'd': 6, 'e': 1}
num_transactions = 20  # Define a small number for illustration
start_date = datetime(2024, 11, 1)

# Creating transactions data
transaction_data = []
for i in range(1, num_transactions + 1):
    timestamp = start_date + timedelta(hours=random.randint(1, 48))
    # Convert items.keys() to a list before using random.sample
    transaction_items = random.sample(list(items.keys()), random.randint(1, 3))
    quantities = {item: random.randint(1, 5) for item in transaction_items}
    item_quantities_str = ",".join([f"{item}:{quantities[item]}" for item in transaction_items])
    transaction_data.append([i, timestamp.strftime('%Y-%m-%d %H:%M'), item_quantities_str])

# Save to CSV
transactions_df = pd.DataFrame(transaction_data, columns=['TransactionID', 'Timestamp', 'Item_Quantities'])
transactions_df.to_csv('transactions.csv', index=False)

# Creating external utilities (separate CSV)
utilities_df = pd.DataFrame(list(items.items()), columns=['Item', 'Utility'])
utilities_df.to_csv('external_utilities.csv', index=False)

transactions_df, utilities_df
