# Bankruptcy_prediction

This repository is for predicting company bankruptcy using mock data. I only included the mock code and the real code is in my private github

## Implementation Details

### Data Acquisition & Processing
- Load mock financial and risk data (debt-to-equity, Z-score, news alerts).
- Integrate balance sheet data (from OpenBB or a CSV source).
- Extract economic indicators (inflation, GDP, currency rates) from a mock API.

### Bankruptcy Prediction Model
- Utilize a LightGBM or CNN model for bankruptcy risk analysis.
- Train on historical financial data with a binary target (bankrupt: 1, not bankrupt: 0).

### Real-Time Risk Detection
- Process Bloomberg-style alerts for supplier risk analysis.
- Use NLP to extract risks from economic/news alerts.

### Supplier Stability Dashboard
- Create a Flask/Dash dashboard to display supplier risk (color-coded indicators). And integrate it with LLMs such as GPT4

![image2](https://github.com/user-attachments/assets/f51a277d-2467-4c49-83ea-c33757465857)

### Required Libraries
```bash
pip install pandas numpy requests openai lightgbm torch torchvision transformers dash flask
