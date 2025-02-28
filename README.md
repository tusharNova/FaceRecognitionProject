# Face Recognition using OpenCV and PyQt5

## 📌 Overview
This project is a **real-time face recognition system** built with **OpenCV** and **PyQt5**.  
It detects and recognizes faces from a webcam and displays a message when a known person is identified.

## 🚀 Features
✅ **Real-time Face Recognition** using OpenCV  
✅ **PyQt5 Message Window** to show recognition alerts  
✅ **Automatic message dismissal** after 2 seconds  
✅ **Mirrored Camera View** for natural display  
✅ **Efficient Face Detection** using Haar Cascade  
✅ **LBPH Face Recognition** for accurate results  

---

## 📂 Project Structure 📂 FaceRecognitionProject ┣ 📂 dataset/ 
# Folder to store training images ┣ 📂 models/ 
# Stores trained face model ┣ 📜 face_trainer.py 
# Script to train the face recognizer ┣ 📜 recognize_faces.py 
# Main script to detect and recognize faces ┣ 📜 README.md 
# Project documentation ┗ 📜 requirements.txt 
# List of required Python libraries

---

## 🔧 Installation

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.7+** installed, then run:
```bash
pip install -r requirements.txt
pip install opencv-python numpy pyqt5


```
🖼️ How It Works
1️⃣ Collect Face Data → Store images in the dataset/ folder.
2️⃣ Train the Model → Run face_trainer.py to generate face_trained.yml.
3️⃣ Recognize Faces → Run recognize_faces.py, and the program will:

- Detect faces in real-time
- Recognize known faces
- Display a PyQt5 message box with the person's name (auto-closes after 2 seconds)


📌 Requirements
✔ Python 3.7+
✔ OpenCV (opencv-python)
✔ NumPy (numpy)
✔ PyQt5 (pyqt5)



🛠️ Future Improvements
🔹 Improve accuracy with deep learning models (e.g., FaceNet, Dlib)
🔹 Database integration for storing recognized faces
🔹 Multiple camera support

👨‍💻 Author
[Tush (Tushar M)]
📧 Email: [tusharmankar@gmail.com]
🔗 GitHub: [Your GitHub Profile]