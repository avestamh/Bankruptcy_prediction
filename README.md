# Bankruptcy_prediction
## IN PROGRESS WITH NONSENSITIVE DATA AND CODES
This repository is used to predict company bankruptcy using mock data. I only included the mock code, and the real code is in my private GitHub

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


## Save the extracted data from D&B in Azure:
# **D&B API Data Fetch and Azure Blob Storage Upload**

This project fetches company data from the **D&B API**, saves a portion of the response as a JSON file, and uploads it to **Azure Blob Storage**.

---

## **Prerequisites**

### **1️⃣ Install Required Python Packages**
Ensure you have the necessary Python packages installed:
```bash
pip install requests azure-storage-blob python-dotenv
```

### **2️⃣ Set Up `.env` File**
Create a `.env` file in the root directory with your **D&B API credentials** and **Azure Storage connection string**:
```ini
# D&B API Credentials
DNB_CLIENT_ID=your_client_id_here
DNB_CLIENT_SECRET=your_client_secret_here

# Azure Storage Connection String
AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
```

---

## **🔹 Steps to Run the Script**

### **1️⃣ Activate Python Environment**
If using **Conda**, activate your environment:
```bash
conda activate AI_torch_gpu
```

---

### **2️⃣ Run the Script**
Execute the script to fetch company data and upload it to **Azure Blob Storage**:
```bash
python fetch_company_data.py
```

---

## **🔹 What the Script Does**
**Fetches company data for "Scania"** from the **D&B API** using a `POST` request.  
**Saves the first company result** to `scania_company.json`.  
**Uploads `scania_company.json` to Azure Blob Storage** under the `supplier-data` container.  

---

## **🔹 Azure Blob Storage Setup (If Not Done Already)**

### **1️⃣ Create an Azure Storage Account**
1. Go to [Azure Portal](https://portal.azure.com/).
2. Navigate to **Storage Accounts** → Click **+ Create**.
3. Enter a **Storage Account Name** (e.g., `dnbstorage123`).
4. Select **Region**, **Standard Performance**, and **StorageV2**.
5. Click **Review + Create** → **Create**.

### **2️⃣ Create a Blob Storage Container**
1. Inside your **Azure Storage Account**, go to **Containers**.
2. Click **+ Container**.
3. Name it **`supplier-data`**.
4. Set **Access Level: Private**.
5. Click **Create**.

---

## **🚀 Expected Output**
```bash
 Sending request to D&B API...
 First company retrieved: Scania AB
 Company data saved as scania_company.json
 File uploaded to Azure: scania_company.json
 Data retrieval & upload complete.
```

---

## **🔹 Troubleshooting**
### **1️⃣ `ModuleNotFoundError: No module named 'azure'`**
Make sure **Azure SDK** is installed:
```bash
pip install azure-storage-blob
```

### **2️⃣ `400 - Requested product is outside contracted product`**
Your D&B API subscription **may not have access** to the requested product. Contact **D&B support**.

### **3️⃣ Azure Upload Fails**
- Ensure **Azure Storage connection string** in `.env` is correct.
- Confirm that **container name (`supplier-data`) exists** in Azure.

---

## **At the end!**
Run the script, and your **D&B API data** will be fetched, saved, and uploaded to **Azure Blob Storage**. 🚀🎉

