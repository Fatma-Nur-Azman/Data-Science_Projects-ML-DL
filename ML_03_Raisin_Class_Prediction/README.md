# 🍇🍇 Raisin Class Prediction using Logistic Regression, KNN, SVM, and Decision Tree 🍇🤖

Welcome to the Raisin Class Prediction project! This project aims to classify two different varieties of raisins (Kecimen and Besni) grown in Turkey using various machine learning techniques.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Project Description](#project-description)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
5. [Modeling](#modeling)
    - [Logistic Regression](#logistic-regression)
    - [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
    - [Support Vector Machine (SVM)](#support-vector-machine-svm)
    - [Decision Tree](#decision-tree)
6. [Model Comparison](#model-comparison)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [About Me](#about-me)
10. [License](#license)

## Introduction

<img src="https://github.com/Fatma-Nur-Azman/Machine_Learning_Projects_ML/blob/main/ML_03_Raisin_Class_Prediction/raisin_class.png">

## Dataset

The dataset used in this project contains 900 samples with 8 features each. The features include:

1. **Area**: Number of pixels within the boundaries of the raisin grain.
2. **Perimeter**: Distance between the boundaries of the raisin grain and the surrounding pixels.
3. **MajorAxisLength**: Length of the main axis, the longest line that can be drawn on the raisin grain.
4. **MinorAxisLength**: Length of the small axis, the shortest line that can be drawn on the raisin grain.
5. **Eccentricity**: Measure of the eccentricity of the ellipse that has the same moments as the raisins.
6. **ConvexArea**: Number of pixels of the smallest convex shell of the region formed by the raisin grain.
7. **Extent**: Ratio of the region formed by the raisin grain to the total pixels in the bounding box.
8. **Class**: Type of raisin grain (Kecimen or Besni).

## Project Description

In this study, a machine vision system was developed to distinguish between two different varieties of raisins (Kecimen and Besni). A total of 900 raisin grains were obtained, with an equal number of samples from each variety. These images were subjected to various preprocessing steps, and 7 morphological feature extraction operations were performed using image processing techniques. The distributions of both raisin varieties on the features were examined and shown in graphs. Later, models were created using Logistic Regression, KNN, SVM, and Decision Tree machine learning techniques, and their performance was evaluated.

## Exploratory Data Analysis (EDA)

The EDA section involves:
- **Understanding The Data**: Basic statistics and distributions of the dataset.
- **Detection of Outliers**: Identifying and handling outliers in the data.
- **Correlation**: Examining the relationships between different features.

## Modeling

### Logistic Regression
Logistic Regression was applied to classify the raisin types. Different preprocessing steps and hyperparameter tuning were performed to improve the model performance.

### K-Nearest Neighbors (KNN)
KNN was used to classify the raisin types based on the nearest neighbors. The model was optimized by tuning the number of neighbors and distance metrics.

### Support Vector Machine (SVM)
SVM was employed to find the optimal hyperplane that separates the two classes. Various kernels and parameters were tested to achieve the best performance.

### Decision Tree
Decision Tree classifier was used to create a model that predicts the class based on feature splits. The model was fine-tuned by adjusting the tree depth and other parameters.

## Model Comparison

The performance of the models was compared using metrics such as accuracy, precision, recall, and F1-score. Confusion matrices and ROC curves were plotted to visualize the results.

## Usage

To use this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Fatma-Nur-Azman/Machine_Learning_Projects_ML.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ML_03_Raisin_Class_Prediction
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Jupyter notebook:
    ```bash
    jupyter notebook Logistic-KNN-SVM-Desicion Tree (Raisin_Class_Prediction).ipynb
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
