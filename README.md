# 🌱 Tuber Crop Analysis Dashboard

This project is an interactive dashboard designed to analyze **tuber crop production** across multiple plants.

It provides insights into agricultural performance using key metrics such as yield, defects, rejection rates, and quality indicators. The dashboard enables users to explore and compare different crop combinations (Variety, Type, Region) in a clear and intuitive way.

---

## 📊 Features

- Data cleaning and aggregation using **pandas**
- Interactive dashboard built with **Streamlit**
- KPI visualization (mean, max, min values)
- Ranking of crop combinations
- Visual analysis of crop quality using:
  - Yield (**Rendimiento**)
  - Total defects (**DT**)
  - Dry damage (**D_seco**)
  - Solids (**Solidos**)
  - Rejection (**Rechazo**)
  - Variance (**Varianza**)
  - Discount (**Descuento**)
- "Traffic light" visualization (Red / Yellow / Green zones)

---

## 🧠 Objective

The goal of this project is to simulate a real-world **agricultural data analysis scenario**, where decisions can be made based on crop quality and production performance.

This type of analysis is commonly used in agro-industrial environments to optimize yield, improve quality, and reduce production losses.

---

## 📁 Project Structure

tuber-crop-dashboard/
│
├── data/
│   ├── planta_alpha.csv
│   ├── planta_beta.csv
│   └── planta_gamma.csv
│
├── dashboard.py
├── analysis.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/tuber-crop-dashboard.git
cd tuber-crop-dashboard

Install dependencies:

pip install -r requirements.txt

---

## ▶️ Run the Dashboard

streamlit run dashboard.py

The application will open in your browser at:

http://localhost:8501

---

## 📈 Example Use Case

A user can:

- Select a plant dataset (Alpha, Beta, Gamma)
- Analyze crop performance
- Identify the best and worst crop combinations
- Evaluate quality indicators visually
- Support decision-making in agricultural production

---

## 🛠️ Technologies Used

- Python
- pandas
- Streamlit
- matplotlib
- openpyxl

---

## 🚀 Future Improvements

- Add filters by region, variety, and type
- Deploy the dashboard online
- Integrate predictive models for yield estimation
- Improve UI/UX design and interactivity

---

## 👩‍💻 Author

Adriel Yulissa Hernandez Albarran

---

## ⭐ Notes

This project is part of a data analysis portfolio and demonstrates skills in:

- Data cleaning and transformation  
- Data visualization  
- Dashboard development  
- Real-world problem solving  

---