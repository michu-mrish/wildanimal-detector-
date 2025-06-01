🐾 Wild Animal Detection & Alert System
A Django-based web platform that enables users to detect and monitor wild animal presence in their locality using AI-powered video analysis. This system is designed to enhance public safety and enable real-time tracking and response by forest authorities.

🌟 Features
👤 User Roles
Civilians / Farmers

Report animal sightings or attacks.

View safety guidelines and tips.

Contact local authorities.

Forest Officers (Authority)

Access real-time dashboard.

Monitor live video feeds from trail cameras.

Track wild animal movements (AI checks every 5 seconds).

Respond to reports from civilians.

🖥️ Dashboard Includes:
Home

Report Incident

Contact Authorities

Guidelines & Safety Tips

🔐 Authentication
Separate login/signup for:

Civilians / Farmers

Forest Officers

🧠 AI-Powered Detection
Integrated AI model continuously analyzes video feeds from trained trail cameras.

Detects and classifies wild animals in the footage every 5 seconds.

Sends alerts to the dashboard when an animal is detected.

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, JavaScript (Django templates)

AI/ML: Pre-trained Wild Animal Detection Model (runs in background)

Database: SQLite (default, configurable to PostgreSQL or MySQL)

Live Feed: Simulated or integrated with trail camera system

🧪 Installation & Local Setup
Follow the steps below to run the project locally:

1. 📦 Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/wild-animal-detection-system.git
cd wild-animal-detection-system
2. 🐍 Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. 📥 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. ⚙️ Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. 🧑‍💼 Create Superuser (for Admin/Authority)
bash
Copy
Edit
python manage.py createsuperuser
6. 🚀 Run the Server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the application.

📸 How It Works
Trail camera feeds are processed by the AI model every 5 seconds.

If a wild animal is detected, the system logs the event and alerts the forest officer.

Civilian-reported incidents are recorded and tracked in the system dashboard.

📂 Project Structure
perl
Copy
Edit
wild-animal-detection-system/
├── core/                # Main app with views, models, and templates
├── detection_ai/        # AI model and image processing
├── media/               # Uploaded footage/images
├── templates/           # HTML templates
├── static/              # CSS, JS, image files
├── manage.py
└── requirements.txt
