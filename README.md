Personal Finance Dashboard
A Streamlit‑based analytics dashboard for exploring personal financial transactions, visualising spending patterns, and generating insights from real‑world banking data.
This project is part of a broader fintech portfolio focused on data‑driven financial intelligence, secure transaction processing, and user‑centric financial tooling.

Features
CSV Upload
Upload any transaction CSV containing:
date
description
amount
the dashboard automatically parses and cleans the data.

Spending by Category
Transactions are categorised using a custom rule‑based classifier.
A Plotly bar chart visualises total spending across categories such as:
Groceries
Transport
Entertainment
Subscriptions
Bills
Income

Monthly Cashflow Analysis
A grouped bar chart shows:
Total monthly income
Total monthly spending
Net cashflow trends
This gives a clear picture of financial health over time.

Clean, Modern Dashboard Layout
The UI uses a two‑column layout:
Left: Raw + categorised transactions
Right: Category spending chart
Bottom: Monthly cashflow
Designed for readability and a professional fintech feel.

Tech Stack
Python
Streamlit — interactive dashboard framework
Pandas — data cleaning + transformation
Plotly Express — interactive visualisations
Custom categorisation logic — rule‑based NLP-style tagging

How to Run Locally
1. Clone the repository
Code
git clone https://github.com/419reggie/Personal-Finance-Dashboard.git
cd Personal-Finance-Dashboard
2. Install dependencies
Code
pip install -r requirements.txt
3. Run the Streamlit app
Code
streamlit run app.py
4. Upload your CSV
Use the file uploader in the UI to load your transactions.

Example CSV Format
Code
date,description,amount
2024-01-02,Tesco groceries,-45.20
2024-01-03,Uber ride,-12.50
2024-01-05,Salary payment,2500
2024-01-07,Netflix subscription,-9.99

Author
Reginald  
Master’s student in Fintech 
