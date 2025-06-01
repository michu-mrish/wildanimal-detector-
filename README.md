# 🐾 Wild Animal Detection & Alert System

**Wild Animal Detection & Alert System** is a full-stack Django web platform designed to detect, monitor, and manage wild animal threats using state-of-the-art AI and video surveillance.

This system is tailored for both **civilians/farmers** and **forest authorities**, ensuring public safety, quick alerts, and proactive wildlife response.

At its core is the powerful **YOLOv8 (You Only Look Once v8)** — a real-time object detection model that enables the platform to detect and classify animals from trail camera feeds every few seconds.

---

## 🔑 Key Features

### 🔐 Secure Role-Based Authentication

Separate login/signup portals for:

- Civilians / Farmers  
  > Report sightings, access safety tips, and contact forest officers.

- Forest Officers  
  > Access detection alerts, live feeds, and track incidents.

---

### 🖥️ Dual Dashboards

**1. Civilian/Farmer Dashboard**

- Report wild animal incidents with details and location
- Access safety guidelines and tips
- Contact local forest authorities directly

**2. Forest Officer Dashboard**

- View live trail camera feeds from the region
- Get automatic AI alerts every 5 seconds
- Monitor public reports and respond efficiently
- Track logs of previous incidents and animal movements

---

### 🧠 AI-Powered Detection (YOLOv8)

- Uses YOLOv8 object detection model for high accuracy and real-time inference
- Processes camera frames every 5 seconds in the background
- Classifies animals and sends immediate alerts to authorities
- Operates seamlessly within the backend architecture

---

## 🛠️ Full-Stack Architecture

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **AI Module**: YOLOv8 object detection (Python-based)
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)

---

## 📡 Real-Time Surveillance System

- Connects to live trail/CCTV cameras
- AI scans feeds every 5 seconds automatically
- Detection logs are stored for later analysis
- Optional: GPS tagging of detections (planned)

---

## 🗃️ Incident Management

- Civilians can submit detailed sightings with optional images
- Authorities can mark reports as resolved and take actions
- Incident logs include:
  - Reporter identity
  - Date/time
  - Animal type
  - Response notes

---

## 🌍 Planned Enhancements

- Google Maps integration for detection mapping
- Push notifications for users in nearby areas
- SMS/email alerts during threats
- YOLOv8 retraining for regional species
- Cloud deployment (AWS/Heroku)
- Mobile app version for rural accessibility

---

## ✅ Testing & Evaluation

- Automated testing using `pytest` and Django test tools
- Sample images/videos included to test AI module
- Manual vs AI alert comparison for accuracy validation

---

## 🚀 Installation & Local Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/wild-animal-detection-system.git
cd wild-animal-detection-system
```

### Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

Visit the application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---
