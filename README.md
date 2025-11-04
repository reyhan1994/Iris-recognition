# Iris Recognition Using Deep Learning

## 🧠 About the Project
This repository presents an **iris recognition system** developed using deep learning techniques.  
The main goal is to achieve **accurate and robust iris identification** by leveraging convolutional neural networks and advanced embedding approaches such as **MobileNet**, **ArcFace**, and **Triplet Loss**.

The project demonstrates expertise in **biometric recognition**, **deep learning model design**, and **margin-based loss optimization** for improving feature discrimination in iris images.

---

## 🧾 Related Publication
This repository is associated with the following research paper:

> **R. Alinia Lat**, S. Danishvar, H. Heravi, and M. Danishvar,  
> *Boosting Iris Recognition by Margin-Based Loss Functions*,  
> **Algorithms**, vol. 15, no. 4, p. 118, 2022.  
> [https://doi.org/10.3390/a15040118](https://doi.org/10.3390/a15040118)

This repository provides the implementation framework and experimental results inspired by the methodology presented in the above paper.  
The study introduces a **margin-based loss function** designed to enhance feature discrimination and improve iris recognition accuracy using deep neural networks.

---

## 🚀 Features
- Iris image preprocessing and segmentation  
- Deep feature extraction using CNN architectures  
- Implementation of ArcFace and Triplet Loss for discriminative learning  
- Training and evaluation pipelines using TensorFlow/Keras  
- Visualization of results with accuracy metrics and confusion matrices  
- Reproducible and modular code structure for research extension  

---

## 📂 Project Structure
```Iris-recognition/
│
├── datasets/ # Iris image datasets
│
├── notebooks/ # Jupyter notebooks for experiments and analysis
│ ├── train_test_split.ipynb
│ ├── segment_sohaib.ipynb
│ └── ...
│
├── models/ # Pretrained models and architecture definitions
│
├── losses.py # Custom loss functions (e.g., Triplet Loss)
│
├── requirements.txt # Python dependencies
│
└── README.md # Project documentation


