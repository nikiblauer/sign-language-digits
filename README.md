# **Sign Language Digit Classification**

This project focuses on classifying hand gestures representing digits (0-9) in sign language using a convolutional neural network (CNN) built with PyTorch. The model is trained on images of hand signs, enabling accurate digit recognition for potential use in accessibility tools or real-time applications.

---

## 🗂️ **Project Structure**

```
├── data/
│   ├── images/              # Hand sign images
│   ├── train.csv            # Training annotations
│   └── test.csv             # Test annotations
├── model.ipynb              # Notebook for data processing, training, and evaluation
├── model.pth                # saved model weights
├── environment.yml          # Conda environment setup
└── README.md                # Project overview
```

---

## 📝 **Task Description**

The goal is to recognize digits (0-9) from sign language images. The notebook covers:  
✅ Dataset exploration and visualization  
✅ Data preparation and augmentation  
✅ CNN architecture for classification  
✅ Model training, evaluation, and predictions  

---

## 🚀 **Getting Started**

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/sign-language-digit-classification.git
   cd sign-language-digit-classification
   ```

2. Create the environment:

   ```bash
   conda env create -f environment.yml
   conda activate sign-language-classification
   ```

3. Run the notebook:

   ```bash
   jupyter notebook model.ipynb
   ```

---

## 📈 **Results**

The model achieves high accuracy on the test set, effectively recognizing sign language digits from images.

