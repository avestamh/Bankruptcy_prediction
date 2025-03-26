'''
This file is generating 100 random sample entries for the important parameters in a company bankruptcy.
use this when you do not have access to actual data and only want to learn the process
'''
import pandas as pd
import numpy as np

# Set a fixed random seed for reproducibility
SEED_VALUE = 42
np.random.seed(SEED_VALUE)

# Define the number of companies
num_stable = 50
num_bankrupt = 50

# Generate random tickers
stable_tickers = [f"STB{i}" for i in range(1, num_stable + 1)]
bankrupt_tickers = [f"BNK{i}" for i in range(1, num_bankrupt + 1)]

# Company sectors (randomly assigned)
sectors = ["Automotive", "Technology", "Retail", "Energy", "Manufacturing", "Finance"]

# Function to generate synthetic financial data
def generate_synthetic_data(num_companies, bankrupt=False):
    np.random.seed(SEED_VALUE + (99 if bankrupt else 0))  # Ensure different seeds for stable vs bankrupt
    
    data = {
        "ticker": [f"BNK{i}" if bankrupt else f"STB{i}" for i in range(1, num_companies + 1)],
        "company_name": [f"Company_{i}" for i in range(1, num_companies + 1)],
        "sector": np.random.choice(sectors, num_companies),

        # Financial Health
        "debt_to_equity": np.random.normal(0.8 if not bankrupt else 3.5, 0.5, num_companies),
        "current_ratio": np.random.normal(1.8 if not bankrupt else 0.7, 0.3, num_companies),
        "altman_z_score": np.random.normal(3.0 if not bankrupt else 1.2, 0.7, num_companies),
        "revenue": np.random.randint(100_000_000, 50_000_000_000, num_companies),
        "ebit": np.random.randint(10_000_000, 5_000_000_000, num_companies),
        "operating_cash_flow": np.random.randint(20_000_000, 10_000_000_000, num_companies),
        "market_cap": np.random.randint(500_000_000, 100_000_000_000, num_companies),

        # Risk Indicators
        "inflation_rate": np.random.normal(3.0 if not bankrupt else 7.5, 1.5, num_companies),
        "currency_volatility": np.random.normal(0.02 if not bankrupt else 0.15, 0.01, num_companies),
        "news_risk_score": np.random.uniform(0.1, 0.4 if not bankrupt else 0.7, num_companies),
        
        # Label for bankruptcy
        "bankrupt": [0] * num_companies if not bankrupt else [1] * num_companies
    }
    
    return pd.DataFrame(data)

# Generate data for stable and bankrupt companies
df_stable = generate_synthetic_data(num_stable, bankrupt=False)
df_bankrupt = generate_synthetic_data(num_bankrupt, bankrupt=True)

# Combine both datasets
df_synthetic = pd.concat([df_stable, df_bankrupt], ignore_index=True)

# Save to CSV
df_synthetic.to_csv("synthetic_bankruptcy_data.csv", index=False)

# Display first few rows
print(df_synthetic.head())
