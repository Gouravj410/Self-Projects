# Iris Flower Classification 🌸

This project is about classifying iris flowers into three species — **Setosa, Versicolor, and Virginica** — based on the measurements of their petals and sepals.

## 📌 Objective
To build and compare machine learning models (Logistic Regression and K-Nearest Neighbors) for classifying iris flowers using the classic Iris dataset.

---

## 📂 Dataset
- **Source:** Scikit-learn's built-in Iris dataset  
- **Features:**
  - Sepal length
  - Sepal width
  - Petal length
  - Petal width
- **Target:** Species of Iris flower

---

## ⚙️ Steps Performed
1. Loaded and explored the dataset (scatter plots, histograms, etc.)
2. Split the dataset into **training** and **test sets**
3. Preprocessed data (clean and ready in sklearn Iris dataset)
4. Trained two models:
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
5. Evaluated models using:
   - Accuracy
   - Confusion Matrix

---

## 📊 Results
- **Logistic Regression:** Achieved good accuracy and clear decision boundaries
- **KNN (k=5):** Also performed well, sometimes slightly better in accuracy

✅ Both models are effective, but **KNN handled class boundaries more flexibly**.

---

## 🛠️ Skills Learned
- Data visualization with **Matplotlib & Seaborn**
- Dataset handling using **Scikit-learn**
- Supervised learning algorithms:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
- Model evaluation:
  - Accuracy Score
  - Confusion Matrix
- Python for Data Science

---

## 🚀 How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/your-username/iris-classification.git
   cd iris-classification
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook  
   ```bash
   jupyter notebook iris.ipynb
   ```

---

## 📌 Future Improvements
- Try more models (Decision Tree, Random Forest, SVM)
- Hyperparameter tuning for KNN and Logistic Regression
- Deploy the best model with a simple web app

---

## 🖊️ Author
Made with ❤️ by Gourav Jangid
