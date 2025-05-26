# AI-NIDS – AI-Powered Intrusion Detection System

AI-NIDS is an AI-based Network Intrusion Detection System that uses machine learning to identify network threats and attacks in real-time. This project utilizes the **NSL-KDD** dataset and applies a **Random Forest classifier** to detect anomalies and classify traffic as normal or attack.

---

## 📊 Dataset

- **Name**: NSL-KDD
- **Source**: [Kaggle - NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd)
- The dataset is a refined version of the classic KDD’99 dataset, commonly used for evaluating intrusion detection systems.

---

## 🧠 Features

- Preprocessing and encoding of categorical data (`protocol_type`, `service`, `flag`)
- Binary classification: `normal` vs `attack`
- Model training using **Random Forest**
- Model evaluation: Accuracy, Confusion Matrix, Classification Report
- Easily extendable to other models (SVM, XGBoost, etc.)

---

## 🚀 How to Run

1. Open the Jupyter notebook / Colab file: `AI-NIDS.ipynb`
2. Download and load the NSL-KDD dataset using Kaggle API
3. Preprocess the dataset
4. Train and evaluate the Random Forest model
5. View results and performance metrics

---

## 🔧 Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- Kaggle CLI (for downloading the dataset)

Install required libraries using:

```bash
pip install pandas numpy scikit-learn seaborn matplotlib kaggle
