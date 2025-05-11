# 🏋️‍♂️ AI Fitness Trainer

A real-time AI-powered fitness trainer that uses computer vision to recognize over 20 exercises, provide live feedback, count repetitions, and generate personalized workout insights. Built using Python, OpenCV, and deep learning.

---

## 🎥 Demo

> ![Screenshot 2025-04-20 214954](https://github.com/user-attachments/assets/2d6a8c2d-726a-46f7-8fff-8f11ad1e822e)

---

## 🚀 Features

- 🧠 Exercise classification (20+ types)
- 🔄 Rep counting with real-time feedback
- 📷 Webcam-based form detection
- 📊 Progress visualization and summary reports
- 📅 Personalized workout planning

---

## 🧰 Tech Stack

| Component         | Technology                     |
|------------------|--------------------------------|
| Language         | Python                         |
| Computer Vision  | OpenCV, Mediapipe              |
| Deep Learning    | TensorFlow / PyTorch           |
| Visualization    | Streamlit / Matplotlib         |
| Dataset          | Custom pose dataset / OpenPose |

---

## 🗂️ Project Structure

```

ai-fitness-trainer/
├── models/               # Trained classification models
├── data/                 # Collected training datasets
├── streamlit\_app/        # UI for live demo
├── utils/                # Pose estimation, feedback logic
├── notebooks/            # Model training and evaluation
└── README.md

````

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yashgolani28/ai-fitness-trainer.git
   cd ai-fitness-trainer

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**

   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## 🧠 How It Works

1. **Pose Estimation**: Uses Mediapipe to extract body landmarks
2. **Classification**: A trained ML model identifies the exercise type
3. **Repetition Logic**: Custom algorithm detects movement direction to count reps
4. **Feedback**: Real-time form correction tips are displayed on screen

---

## 📈 Model Training

You can retrain the model on new exercises:

```bash
cd notebooks/
python train_model.py --epochs 50 --data data/
```

---

## 📬 Contributors

* Yash Golani

---

## 💬 Contact

Connect on [LinkedIn](https://www.linkedin.com/in/yashgolani28) or raise an issue for suggestions and improvements!

```
