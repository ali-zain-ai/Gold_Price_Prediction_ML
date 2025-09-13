# Gold Price Prediction using Machine Learning
# 📌 Overview

This project focuses on predicting gold prices (GLD values) using historical financial indicators.
Gold is a crucial global asset, often used as a hedge against inflation. Forecasting its price provides valuable insights for investors, analysts, and policymakers.

A Random Forest Regressor has been trained on financial market data to capture relationships between multiple factors and predict gold prices with reasonable accuracy.

# 📊 Dataset

The dataset contains historical gold prices along with other financial indicators.

Date → Timestamp of recorded values (dropped during preprocessing)

GLD → Actual Gold Price (target variable)

Financial Indicators → Features such as stock indices, commodity prices, and macroeconomic values influencing gold prices

(Exact features depend on the CSV columns, excluding Date and GLD.)

# ⚙️ Data Preprocessing

Target Selection → GLD column used as the prediction target

Feature Selection → All columns except Date and GLD used as predictors

Data Split → 80% training, 20% testing using train_test_split

# 🤖 Model

The model chosen is Random Forest Regressor, which combines multiple decision trees to improve accuracy and reduce overfitting.

Algorithm → Random Forest Regression

Max Depth → 3 (to control complexity)

Train-Test Split → 80/20

# 📈 Evaluation

Metric Used → R² Score (Coefficient of Determination)

Interpretation:

R² ≈ 1 → Strong predictive power

R² ≈ 0 → Weak predictive power

R² < 0 → Model performs worse than baseline (mean prediction)

The script prints both the R² score and model accuracy (in %).

Example Output:

0.9234
Model Accuracy = 92.34%

# 🚀 Applications

Financial Analysis → Forecasting gold prices based on market indicators

Investment Decisions → Supporting investors with risk assessment

Economic Research → Studying macroeconomic influences on gold trends

# 🔮 Future Enhancements

Train deeper Random Forests or advanced models (e.g., Gradient Boosting, XGBoost, LSTM for time-series forecasting)

Perform feature importance analysis to identify strongest predictors

Apply rolling-window cross-validation for time-series validation

Add visualizations comparing predicted vs. actual gold prices

✨ This project demonstrates the use of machine learning in financial forecasting, offering a foundation for more advanced time-series modeling.
