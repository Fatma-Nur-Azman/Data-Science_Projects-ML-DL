# Adult Income Prediction Project 💼💰

Welcome to the Adult Income Prediction project! This project uses machine learning techniques to classify individuals' income levels based on demographic and employment-related attributes. The goal is to predict whether a person earns more than $50K a year.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
4. [Feature Engineering](#feature-engineering)
5. [Models](#models)
    - [Logistic Regression](#logistic-regression)
    - [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
    - [Support Vector Machine (SVM)](#support-vector-machine-svm)
6. [Model Comparison](#model-comparison)
7. [Conclusion](#conclusion)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [About Me](#about-me)
11. [License](#license)

## Introduction

<img src="https://github.com/Fatma-Nur-Azman/Machine_Learning_Projects_ML/blob/main/ML_04_Adult_Income_Prediction/adult_.png">

## Dataset

- **Source:** UCI Machine Learning Repository
- **Rows:** 32,561
- **Columns:** 15
- **Attributes:** 
    - Age, Workclass, fnlwgt, Education, Education Number, Marital Status, Occupation, Relationship, Race, Sex, Capital Gain, Capital Loss, Hours per Week, Native Country, Income

## Exploratory Data Analysis (EDA)

The EDA section includes:
- **Understanding The Data:** Basic statistics and distribution analysis.
- **Handling Missing Values:** Imputing or removing missing values.
- **Detection of Outliers:** Identifying and handling outliers in the data.
- **Correlation Analysis:** Exploring the relationships between different numerical features.

## Feature Engineering

Various feature engineering steps were performed, such as:
- **Categorical Features:** Encoding categorical variables using OneHotEncoder and OrdinalEncoder.
- **Numerical Features:** Scaling numerical variables using StandardScaler.
- **Feature Creation:** Creating new features from existing ones to enhance model performance.


## Models

### Logistic Regression
A Logistic Regression model was built and optimized using GridSearchCV to predict the income level. The model was evaluated using confusion matrices, ROC curves, and precision-recall curves.

### K-Nearest Neighbors (KNN)
A KNN model was applied, and the optimal number of neighbors was selected using the Elbow Method. The model was evaluated with similar metrics as Logistic Regression.

### Support Vector Machine (SVM)
The SVM model was trained using different kernels, and hyperparameters were tuned using GridSearchCV. Performance metrics include confusion matrices, ROC curves, and precision-recall curves.

## Model Comparison

The performance of all models was compared based on metrics such as accuracy, precision, recall, and F1-score. The results were visualized using confusion matrices, ROC curves, and precision-recall curves.

## Conclusion

The project concludes by summarizing the performance of each model and discussing potential improvements and future work.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Fatma-Nur-Azman/Machine_Learning_Projects_ML.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ML_04_Adult_Income_Prediction
    
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Jupyter notebook:
    ```bash
    jupyter notebook Adult_Income_Prediction (Logistic-KNN-SVM).ipynb
    ```

## Contributing

We welcome contributions! If you'd like to contribute, please follow these guidelines:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## About Me

Hello! I'm Fatma NUr AZMAN, a data analytics and data science enthusiast.

📊 Data Detective: Getting lost in data and turning it into meaningful insights is my hobby. Playing with data and deciphering its language is my superpower!

☕ Coffee Lover: I always have a cup of coffee by my side while analyzing data. Good coffee fuels my creativity.

🎵 Music Enthusiast: Light jazz music playing in the background keeps me motivated while analyzing data. Music helps me stay focused and productive.

🧩 Puzzle Master: I solve puzzles to keep my mind active. This helps improve my analytical thinking skills.

📧 Contact

- [LinkedIn](https://www.linkedin.com/in/fatma-nur-azman/)
- [GitHub](https://github.com/Fatma-Nur-Azman)
- [Website](https://fatmanurazman.vercel.app/)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Ready to embark on a journey in the world of machine learning with raisins? 🍇🚀 If you find this repository helpful, don't forget to ⭐ star it!

Happy Coding! 💻✨
