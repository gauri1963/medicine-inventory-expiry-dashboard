# medicine-inventory-expiry-dashboard
Medicine Inventory &amp; Expiry Tracking Dashboard using Python(streamlit), MySQL and Power BI
 Pharmacy Inventory Analysis Project

A complete Python-based pharmacy inventory analysis project that combines data cleaning, visualization, dashboarding, and optional database storage.

## Project Overview
This project analyzes pharmacy inventory data from an Excel workbook and a CSV export. It helps identify:
- low-stock medicines
- expired or expiring medicines
- category-wise inventory distribution
- supplier and warehouse insights

## Features
- Reads Excel files with multiple sheets
- Cleans and transforms pharmaceutical inventory data
- Calculates expiry status and stock-related insights
- Creates charts using Matplotlib and Seaborn
- Builds a Streamlit dashboard
- Stores cleaned data into MySQL (optional)

## Project Files
- app.py - Streamlit dashboard application
- Medicine inventory and pharmacy .py - main analysis and preprocessing script
- final_pharmacy_data.csv - cleaned inventory dataset
- pharmacy_star_schema2.xlsx - source Excel workbook
- requirements.txt - Python dependencies
- project_report.md - project summary and explanation

## Installation
Clone the project and install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Dashboard
Start the Streamlit app with:

```bash
streamlit run app.py
```
## 📊 Dashboard Preview

### 1. Dashboard Overview
[Overview screenshot]

### 2. Inventory & Expiry Analytics
[Analytics screenshot]

### 3. Detailed Inventory Analysis
[Detailed screenshot]

## Run the Analysis Script
You can also run the Python analysis script directly:

```bash
python "Medicine inventory and pharmacy .py"
```

## Requirements
The project uses these Python libraries:
- streamlit
- pandas
- plotly
- mysql-connector-python
- openpyxl
- matplotlib
- seaborn

## Notes
- The project uses sample pharmacy inventory data.
- You can connect it to a real MySQL database by updating the connection settings in the Python script.
- A Power BI version can be added later for business reporting.

## License
This project is for educational and portfolio purposes.
