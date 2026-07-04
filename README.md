# 🌍 LandVision AI

**LandVision AI** is an AI-powered land management and visualization platform built using **Django REST Framework**, **Leaflet.js**, and **Groq AI**. It enables users to explore land records on an interactive map, search plots, filter geographic data, and interact with an AI assistant using natural language.

---

## 📖 Project Overview

Managing land records through traditional methods is often slow, error-prone, and difficult to visualize. LandVision AI provides a modern solution by combining Geographic Information Systems (GIS) with Artificial Intelligence.

Users can:

- View land plots on an interactive map
- Filter plots by State, District, Tehsil, and Village
- Search plots instantly
- View ownership and land details
- Ask questions in natural language using AI
- Analyze land statistics

---

## ✨ Features

### 🗺 Interactive GIS Map

- Display land plots using GeoJSON
- Zoom and explore plots
- Interactive popups with plot information

### 🔍 Plot Search

- Search plots by plot number
- View owner details
- View land usage
- Locate plots instantly

### 📍 Geographic Filters

Filter data by:

- State
- District
- Tehsil
- Village

### 🤖 AI Assistant (Groq)

Ask questions like:

- Who owns Plot 102?
- Show Plot 21
- Show all commercial plots
- Tell me about Harpur village
- How many plots are available?

The AI understands natural language, detects user intent, and retrieves data directly from the database.

### 📊 Land Statistics

View statistics including:

- Total plots
- Residential plots
- Agricultural plots
- Commercial plots
- Industrial plots
- Government land

---

# 🏗 Project Structure

```
LandVision-AI/
│
├── backend/
│   ├── ai/
│   ├── plot/
│   ├── village/
│   ├── config/
│   ├── manage.py
│   ├── requirements.txt
│   └── build.sh
│
├── frontend/
│   ├── css/
│   ├── js/
│   └── index.html
│
├── dataset/
├── docs/
└── README.md
```

---

# ⚙ Technology Stack

## Backend

- Python
- Django
- Django REST Framework
- Django Filters
- PostgreSQL
- WhiteNoise

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- Bootstrap 5
- Leaflet.js

## AI

- Groq API
- Llama 3.3 70B Versatile

## Deployment

- Render
- PostgreSQL

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/LandVision-AI.git

cd LandVision-AI/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv env
```

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
SECRET_KEY=your_secret_key

DATABASE_URL=your_database_url

GROQ_API_KEY=your_groq_api_key
```

---

## 5. Apply Migrations

```bash
python manage.py migrate
```

---

## 6. Run Development Server

```bash
python manage.py runserver
```

Backend

```
http://127.0.0.1:8000/
```

---

## 7. Run Frontend

Open

```
frontend/index.html
```

using Live Server or any static server.

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v1/states/` | List all states |
| `/api/v1/districts/` | List districts |
| `/api/v1/tehsils/` | List tehsils |
| `/api/v1/villages/` | List villages |
| `/api/v1/plots/` | Plot information |
| `/api/v1/plots/map/` | GeoJSON map data |
| `/api/v1/ai/chat/` | AI Chat Endpoint |

---

# 🤖 AI Workflow

```
User

↓

Frontend

↓

Django REST API

↓

Groq AI

↓

Intent Detection

↓

AI Tools

↓

Database Query

↓

Natural Language Response

↓

Frontend
```

---

# 📸 Screenshots

You can add screenshots here.

- Dashboard
- Interactive Map
- Plot Popup
- AI Assistant
- Search Functionality

---

# 📈 Future Improvements

- AI-based map navigation
- Voice assistant
- OCR for land documents
- Satellite imagery integration
- PDF report generation
- Authentication & Role Management
- Plot comparison
- Property valuation using AI

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 🐞 Reporting Issues

If you discover any bug or have suggestions, please create an Issue in this repository.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Priyanshu Tripathi**

GitHub: https://github.com/KeepQuite-cyber

Linkedin: https://www.linkedin.com/in/priyanshu-tripathi-66b557341

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
