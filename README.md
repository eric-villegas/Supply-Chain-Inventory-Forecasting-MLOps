# 🚀 Supply-Chain Inventory Forecasting (MLOps)

## 🎯 Business Value Proposition
As an Operations Leader with an MSc in Business Analytics, I bridge the gap between complex data science and bottom-line profitability. This project demonstrates the architecture I've used to achieve:
* **12% Reduction** in inventory costs.
* **$350,000 USD** in projected annual savings.
* **14% Lower** labor costs through data-driven labor models.

## 🏗️ System Architecture (End-to-End)
This repository showcases a production-ready MLOps pipeline designed to handle the "messy" reality of supply chain data:

1. **Bronze Layer (Ingestion):** AWS Lambda triggers on S3 uploads to capture vendor spreadsheets automatically.
2. **Silver Layer (Validation):** Automated data quality checks and cleaning using Python (Pandas) to ensure P&L accuracy.
3. **Gold Layer (Inference):** XGBoost/Prophet forecasting models that calculate safety stock and suggested orders.
4. **Distribution:** A dynamic hierarchical reporting engine that generates tailored PDFs (WeasyPrint) and distributes them via Amazon SES.

## 🛠️ Tech Stack
* **Cloud:** AWS (S3, Lambda, RDS, SES)
* **DevOps:** Terraform (Infrastructure as Code), Docker, GitHub Actions (CI/CD)
* **ML/Data:** Python (Pandas, Scikit-Learn), SQL, Power BI
* **Methodologies:** Lean Six Sigma (Green Belt), Agile/Scrum

## 📈 Proven Impact (Previous Implementations)
* **Foodology:** Optimized critical inventory management for 90+ dark kitchens across 4 countries.
* **Pizza Hut / KFC:** Designed and implemented the first automated supply projection systems for 234+ locations.
* **Nissan:** Standardized high-impact robotic maintenance procedures as a Project Manager.

---
**Contact:** [eric.mavigo@gmail.com](mailto:eric.mavigo@gmail.com) | [LinkedIn: eric villegas](https://www.linkedin.com/in/evillegas90)
