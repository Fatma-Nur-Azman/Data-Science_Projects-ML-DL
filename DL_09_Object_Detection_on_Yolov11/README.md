# Flower Recognition Using CNN and Transfer Learning 🌸🤖

**Dataset Link**: [Flower Recognition Dataset](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)  
**Kaggle Notebook**: [Flowers Rec | CNN | 10 Transfer Learning | Part-2 🌻](https://www.kaggle.com/code/fnurazman/flowers-cnn-10-transfer-learning-part-2)  
**Project Image**:  
<img src="https://github.com/Fatma-Nur-Azman/Data-Science_Projects-ML-DL/blob/main/ML_07_Flowers_Detection/flowers.jpeg" alt="Flower Recognition" width="600">

## Project Overview

This project applies **Convolutional Neural Networks (CNN)** and **Transfer Learning** to classify images of flowers into five categories. The goal is to automate flower identification to support botanical research, education, and conservation efforts using a dataset of flower images sourced online.

## Importance of Automated Flower Recognition

Automated recognition systems play a crucial role in:
- **Cataloging Species**: Helps document and classify plant species efficiently.
- **Monitoring Biodiversity**: Tracks species distribution and changes in ecosystems.
- **Ecological Conservation**: Supports conservation efforts by providing accurate identification.
- **Educational Tools**: Assists in plant classification in botanical education.
- **Agricultural Planning**: Aids in identifying plant species for garden and crop management.

## Project Execution Steps

1. **Image Preprocessing**: Resizing and augmenting images to enhance model performance.
2. **Normalization**: Standardizing pixel values for consistent training.
3. **Model Development**: Using CNN for feature extraction and Transfer Learning to improve model accuracy.
4. **Performance Evaluation**: Iteratively refining the model based on accuracy and other performance metrics.

## Applications and Impact

- **Educational Tools**: Enhancing plant classification in botanical education.
- **Conservation**: Assisting in the documentation and monitoring of plant species.
- **Agricultural Planning**: Helping in the identification of plant species for garden management.

## About the Dataset

The **Flower Recognition Dataset** contains **4,242 images** of flowers from sources like Flickr, Google Images, and Yandex Images. The dataset comprises five flower categories:

- **Classes**: Daisy, Tulip, Rose, Sunflower, Dandelion
- **Resolution**: Approx. 320x240 pixels
- **Total Images**: 4,242
- **Source**: Scraped from Flickr, Google Images, and Yandex Images

The dataset maintains the original proportions of the images, adding complexity and realism to the classification task. It is suitable for both academic research and practical applications in plant recognition. Find the dataset on [Kaggle](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition).

## Project Summary

In this project:

- A detailed exploratory analysis was conducted to:
  - Identify the images in each class.
  - Determine their dimensions.
  - Decide whether scaling was needed.
  - Examine the data distribution across classes.

- For transfer learning models:
  - Base models were created by freezing the pretrained layers.
  - Smaller versions of transfer learning models were selected due to the small to medium-sized dataset to prevent overfitting.
  - Even these smaller models required careful tuning to achieve optimal performance.

## Additional Transfer Learning Models

This study, in collaboration with Duygu Jones, applies a CNN model along with **10 different transfer learning models** to the Flower Recognition dataset. Additional models explored include:

- **VGG16**
- **InceptionV3**
- **NASNetMobile**
- **EfficientNetB3**
- **EfficientNetV2-S**
- **ConvNeXtTiny**

For further details on these models and their implementation, please refer to the **Kaggle notebook** available at this link: [Flowers Rec | CNN | 10 Transfer Learning | Part-2 🌻](https://www.kaggle.com/code/fnurazman/flowers-cnn-10-transfer-learning-part-2).

## Conclusion

This project demonstrates the power of **CNN** and **Transfer Learning** for flower recognition, contributing to applications in **education**, **conservation**, and **agricultural planning**. The use of multiple models allows for a robust comparison, ensuring that the best-performing model is selected for deployment.

---

If you find this project helpful or interesting, please ⭐ star the repository and explore the Kaggle notebook for more insights!

Happy Coding! 🌼✨
