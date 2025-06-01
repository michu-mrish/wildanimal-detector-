# 🐾 Wild Animal Detection & Alert System

Wild Animal Detection & Alert System is an intelligent, full-stack Django web application built to detect, monitor, and manage wild animal threats using state-of-the-art AI and video surveillance. Designed with both civilians/farmers and forest authorities in mind, this platform ensures public safety, real-time response, and proactive wildlife management.

At the heart of this platform is YOLOv8 (You Only Look Once v8) — one of the most accurate and efficient object detection models available — integrated seamlessly into the system to perform real-time animal recognition from trail camera footage.

The system offers:

🔐 Secure Role-Based Authentication
Separate login and signup interfaces for:

🧑‍🌾 Civilians & Farmers – to report sightings and access safety resources.

🌲 Forest Officers – to manage incidents, view detections, and monitor regions.

🧑‍💻 Dual Dashboards with Role-Specific Functionality
1. Civilian/Farmer Dashboard:
📢 Report wild animal incidents with location and details.

🛡️ Access safety guidelines and precautionary tips.

📞 Contact local authorities in emergencies.

2. Forest Officer Dashboard:
🎥 View live camera feeds connected to trail cameras.

🤖 Get AI-powered alerts every 5 seconds for animal detection in videos.

📊 Monitor reported incidents across regions.

📂 Track historical movements and response logs.

🧠 AI-Powered Detection with YOLOv8
Uses YOLOv8, a state-of-the-art real-time object detection model

Continuously analyzes incoming camera frames

Detects wild animals and classifies them by species

Sends instant alerts to the authority dashboard for action

🛠️ Full-Stack Web Architecture
Backend: Django (Python) – handles user management, camera integrations, and AI coordination.

Frontend: Django templates with HTML, CSS, JavaScript – delivers clean, responsive interfaces.

AI/ML Module: Python-based image classification model connected to the backend for video processing.

Database: SQLite (local), scalable to PostgreSQL/MySQL for deployment.

This platform is a powerful demonstration of how modern AI and web development can be used to address real-world problems, supporting both community welfare and forest department operations with intelligence, automation, and user-focused design.
---


📡 Real-Time Surveillance System
🕵️‍♂️ The platform connects to trail or CCTV cameras installed near forest perimeters or rural areas.

🕔 AI processes each frame every 5 seconds to detect animal presence, without needing manual monitoring.

🔁 The feed auto-refreshes, and detection logs are stored for future analysis.

🗺️ Option to integrate GPS mapping for location tagging of animal detections (can be an enhancement for future).

🗃️ Incident Management & Response
📝 Civilians submit sightings or danger reports through a structured form with optional media upload.

🧭 Authorities can view, categorize, and mark incidents as resolved.

📌 Incident records include:

Reporter details

Time & date

Type of animal involved

Action taken by forest officers

📈 Future scope: integrating SMS/email alerts for citizens in affected zones.

🌐 Future Enhancements (Optional Section)
You can include this to highlight the scalability or roadmap:

🌍 Integration with Google Maps API to visualize detection points on a map.

📲 Push notification system for mobile alerts to nearby users.

🧠 Retraining the YOLOv8 model with more regional species for higher accuracy.

☁️ Deploy on cloud platforms like AWS or Heroku for real-time scalability.

📱 Build a companion mobile app for rural users with limited access to desktop browsers.

🧪 Testing & Evaluation
🔄 Unit and integration testing using pytest and Django’s test framework.

📸 Sample image & video datasets are included for verifying the AI detection module.

🧪 Accuracy can be tracked by comparing AI alerts with manual reports.


## 🧪 Installation & Local Setup

### 📦 Clone the Repository

```bash
git clone https://github.com/your-username/wild-animal-detection-system.git
cd wild-animal-detection-system
```

### 🐍 Set Up Virtual Environment

```bash
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🧑‍💼 Create Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

### 🚀 Run the Server

```bash
python manage.py runserver
```

- Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


