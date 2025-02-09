[![GitHub license](https://img.shields.io/github/license/SINGHxTUSHAR/Client-Retention-Insight.svg)](https://github.com/SINGHxTUSHAR/Client-Retention-Insight/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/SINGHxTUSHAR/Client-Retention-Insight.svg)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/SINGHxTUSHAR/Client-Retention-Insight.svg)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SINGHxTUSHAR/Client-Retention-Insight.svg)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


[![GitHub watchers](https://img.shields.io/github/watchers/SINGHxTUSHAR/Client-Retention-Insight.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/SINGHxTUSHAR/Client-Retention-Insight.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/network/)
[![GitHub stars](https://img.shields.io/github/stars/SINGHxTUSHAR/Client-Retention-Insight.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Client-Retention-Insight/stargazers/)

[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/SINGHxTUSHAR/Client-Retention-Insight)


# Client-Retention-Insight:
![preview Image](https://github.com/SINGHxTUSHAR/Client-Retention-Insight/blob/5ed9b2d795bed6e0633b298f0fe3af9da1169873/preview.png)

"Client-Retention-Insight" is a machine learning project designed to predict customer churn using an Artificial Neural Network (ANN) implemented in TensorFlow.
The primary objective is determining whether a customer will likely exit based on various features such as account balance, tenure, credit score, and estimated salary.
Additionally, regression analysis is conducted on the Estimated Salary feature to explore its impact, and Hyperparameter Tuning is performed to optimize the ANN model for better accuracy.
This project is crucial for businesses, particularly in banking, telecom, and subscription-based services, where customer retention is a key metric for profitability. By predicting churn early, businesses can take proactive measures to retain valuable customers.

## Workflow of the Project:

The workflow of the Client-Retention-Insight project follows a structured pipeline for data processing, model building, evaluation, and optimization. Below is a step-by-step breakdown:

1. `Data Collection & Preprocessing Dataset`: The dataset contains customer-related features such as
CreditScore
Geography
Gender
Age
Tenure
Balance
Number of Products
Has Credit Card
Is Active Member
Estimated Salary
Exited (Target variable: 1 for churned customers, 0 for retained customers)
Handling Missing Values: Check for null values and handle them accordingly.
Feature Encoding: Convert categorical variables (e.g., "Geography," "Gender") into numerical representations using one-hot encoding.
Feature Scaling: Normalize or standardize numerical features (e.g., CreditScore, Balance, Estimated Salary) using MinMaxScaler to improve ANN performance.
Splitting Data: Divide the dataset into training and testing sets (e.g., 80%-20% split).


3. `Exploratory Data Analysis (EDA)`
Visualize the distribution of features using histograms, box plots, and KDE plots.
Analyze correlations between variables using heatmaps.
Identify patterns and trends in the data that influence customer churn.


5. `Regression on EstimatedSalary Feature`
Objective: To examine how salary impacts customer churn probability.
Model Used: Linear Regression or Polynomial Regression.
Analysis: Understand the trend between EstimatedSalary and the probability of churn.


7. `Building the ANN Model`
Architecture:
Input Layer: Accepts the preprocessed feature set.
Hidden Layers: Multiple fully connected layers with ReLU activation.
Output Layer: Uses Sigmoid activation to classify whether the customer will exit (1) or stay (0).
Loss Function: Binary Cross-Entropy.
Optimizer: Adam optimizer is used for efficient weight updates.
Evaluation Metric: Accuracy, Precision, Recall, and F1-score.


9. `Model Training & Evaluation`
Train the ANN model using the training dataset.
Validate model performance using test data.
Plot the loss vs. epochs and accuracy vs. epochs graphs to monitor training progress.
Compute confusion matrix, ROC-AUC curve, and classification report.


11. `Hyperparameter Tuning`
Optimize ANN architecture using Grid Search or Random Search.
Parameters tuned:
Number of layers
Number of neurons per layer
Learning rate
Batch size
Dropout rate
Select the best-performing combination of hyperparameters to improve model performance.


13. `Model Deployment & Insights`
Once trained and optimized, the model is tested on new customer data.
Predictions help businesses develop targeted retention strategies.
Model deployment options:
Web-based API (Flask/Django)
Integration into business dashboards

## Workflow Diagram
Here is a diagram representing the end-to-end workflow of the Client-Retention-Insight project:
```
+----------------------+
| Data Collection     |
+----------------------+
           ↓
+----------------------+
| Data Preprocessing  |
| - Handling Missing  |
| - Encoding Features |
| - Scaling Features  |
+----------------------+
           ↓
+----------------------+
| Exploratory Data    |
| Analysis (EDA)      |
+----------------------+
           ↓
+----------------------+
| Regression on       |
| EstimatedSalary     |
+----------------------+
           ↓
+----------------------+
| ANN Model Training  |
| - Input Layer       |
| - Hidden Layers     |
| - Output Layer      |
+----------------------+
           ↓
+----------------------+
| Model Evaluation    |
| - Accuracy          |
| - Precision-Recall  |
| - ROC Curve         |
+----------------------+
           ↓
+----------------------+
| Hyperparameter      |
| Tuning              |
+----------------------+
           ↓
+----------------------+
| Deployment &        |
| Business Insights   |
+----------------------+

```

## Requirements💻 :

Ensure you have the following dependencies installed:

- Python (version 3.11.x || 3.12.x)
- IDE: VS-CODE or collab
- Virtual-environment(venv)
- Other dependencies (refer to the requirement.txt)

You can install the required Python packages using:

```bash
pip install -r requirement.txt
```


## Setup 💿:

- Clone the repository:
```bash
git clone https://github.com/SINGHxTUSHAR/NextWordAI.git
cd Client-Retention-Insight
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Activate the virtual environment:
  - On Windows:
   ```bash
   venv\Scripts\activate
   ```
  - On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```


## Contributing 📌:
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process. Contributions, issues, and feature requests are welcome!

## Suggestion 🚀: 
If you have any suggestions for me related to this project, feel free to contact me at tusharsinghrawat.delhi@gmail.com or <a href="https://www.linkedin.com/in/singhxtushar/">LinkedIn</a>.

## License 📝:
This project is licensed under the <a href="https://github.com/SINGHxTUSHAR/Client-Retention-Insight/blob/main/LICENSE">MIT License</a> - see the LICENSE file for details.
