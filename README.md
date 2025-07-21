# 🛒 Supermarket Sales Analysis (Python CLI Version)

This project performs an **Exploratory Data Analysis (EDA)** on supermarket transaction data using **pure Python and terminal output (no dashboard or web app)**. The purpose is to extract business insights from customer purchases across branches, product lines, and customer demographics.

---

## 📌 Project Summary

This analysis was built using a standalone Python script (`main.py`) that outputs results and insights directly to the terminal, including statistical summaries and visualizations.

---

## 🎯 Goals of the Project

- Analyze revenue trends and top-selling products
- Understand branch-wise sales performance
- Examine customer patterns by type and gender
- Evaluate gross income and profit margins
- Visualize invoice value distribution and monthly trends

---

## 📊 Insights from the Terminal Output

### ✅ Dataset Overview

- **1,000 rows** with **17 features**
- No missing/null values
- Key metrics include: `Total`, `Quantity`, `Gross income`, `Branch`, `Product line`, `Customer type`, and `Rating`.

---

### 🔢 Statistical Summary

- **Average Sale per Invoice:** ~\$322.97
- **Max Invoice Value:** \$1,042.65
- **Average Gross Income per Sale:** ~\$15.38
- **Gross Margin Percentage:** Constant at **4.76%**

---

### 🏆 Top-Selling Product Lines (by Revenue)

1. **Food and Beverages** – \$56,144
2. **Sports and Travel** – \$55,122
3. **Electronic Accessories** – \$54,337

---

### 🏢 Total Sales by Branch

- **Branch C** leads with \$110,568
- Followed by Branch A and B with similar sales (~\$106,200)

---

### 📅 Monthly Sales Trend

| Month | Total Sales    |
|-------|----------------|
| Jan   | \$116,291.87   |
| Feb   | \$97,219.37    |
| Mar   | \$109,455.51   |

**🟢 January** was the best performing month.

---

### 💰 Profitability by Product Line

| Product Line            | Gross Income | Quantity | Revenue       |
|-------------------------|--------------|----------|---------------|
| Food and Beverages      | \$2,673.56   | 952      | \$56,144.84   |
| Sports and Travel       | \$2,624.89   | 920      | \$55,122.83   |
| Electronic Accessories  | \$2,587.50   | 971      | \$54,337.53   |
| Health and Beauty       | \$2,342.56   | 854      | \$49,193.74   |

---

## 🗃️ File Structure

```
supermarket-sales-cli/
│
├── data/
│ └── supermarket_sales.csv # The dataset
├── Visuals/
│ └── Saved Matplotlib images
├── Notebooks/
│ └── supermarket_sales_analysis.ipynb
│
├── main.py # The main EDA script
├── README.md # This file
└── requirements.txt # Python packages
```

----

## ⚙️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/febrianwardi/supermarket-sales.git

2. Navigate into the folder and run:
   
   ```bash
   cd supermarket-sales-analysis
   python main.py

3. The output will be printed in the terminal along with multiple sales visualizations (bar charts, histograms).


---


## 🛠️ Technologies Used
Python 3
Pandas
Seaborn
Matplotlib
Terminal-based output


## 📄 License
This project is open for educational and personal use.

## 🙌 Acknowledgements
Dataset sourced from public Kaggle repositories. Analysis and script developed as a data analytics portfolio project.
