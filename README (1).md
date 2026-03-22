
# Project Title

🎧 Audio Classification and Emotion Detection Sysytem

## 📌 Project Description

This project is Deep Learning based Audio and Emotion Classification System.It can classify audio file and emotion from audio into categories using feature extraction and trained models.

## 📊 Dataset

This project uses the UrbanSound8K dataset for training and testing the audio classification model.

[Download Dataset](https://urbansounddataset.weebly.com/download-urbansound8k.html)

UrbanSound8K is a dataset of urban sounds commonly used for audio classification tasks.
It contains 8732 labeled audio clips of different environmental sounds, each with a duration of ≤ 4 seconds.The dataset is divided into 10 predefined folds.

## 📦 Requirements

This project requires the following Python libraries.

All dependencies are listed in the requirements.txt file.

### Install requirements
Run the following command:pip install -r requirements.txt

### Main Libraries Used

numpy==2.1.0
scipy==1.13.1
pandas==2.2.2
scikit-learn==1.6.1
librosa==0.11.0
matplotlib==3.8.4
virtualenv

## ⚙️ Setup

Follow these steps to setup the project on your system.

### 1. Clone the repository

git clone https://github.com/rosh-pawar1821/audio_classification

cd audio_classification


### 2. Create virtual environment

virtualenv env


### 3. Activate virtual environment

Command Prompt:

env\Scripts\activate

PowerShell:

.\env\Scripts\activate


### 4. Install required libraries

pip install -r requirements.txt


### 5. Download Dataset

Download UrbanSound8K dataset from:

https://urbansounddataset.weebly.com/download-urbansound8k.html

Extract the dataset and place it inside project folder.


### 6. Run the project

python app.py

## 🎯 Inference Demo

After completing the setup, follow the steps below to test the Audio Emotion Classification system.

### Step 1 – Run Django Server

python manage.py runserver


Open browser:

http://127.0.0.1:8000


### Step 2 – Upload Audio File

Go to **Upload Audio for Emotion Detection** page

- Choose audio file (.wav)
- Click Predict


### Step 3 – Model Prediction

The system will:

- Load trained model
- Extract audio features using Librosa
- Predict emotion from audio
- Display predicted emotion on screen


### Example Output

Input: happy.wav  
Output: Predicted Emotion → Happy


## ✨ Features

- Upload audio file for prediction
- Audio emotion classification using trained ML/DL model
- Feature extraction using Librosa
- Real-time prediction using Django web app
- User-friendly web interface
- Supports WAV audio format
- Uses pre-trained model for fast inference
- Displays predicted emotion on screen


## 🛠 Tech Stack

- Python 3.12
- Django
- NumPy
- Pandas
- Scikit-learn
- Librosa
- Matplotlib
- HTML / CSS

## Screenshots

![App Demo](https://raw.githubusercontent.com/rosh-pawar1821/audio_classification/master/demogif.gif)

![Demo1](https://raw.githubusercontent.com/rosh-pawar1821/audio_classification/master/demo1.png)

![Demo2](https://raw.githubusercontent.com/rosh-pawar1821/audio_classification/master/Demo2.png)


## 👤 Author

Roshani Pawar

Passionate about Python, Machine Learning, Deep Learning and Django.  This project is part of my learning in Audio Classification and working with binary data using Librosa, Scikit-learn,keras and Django.