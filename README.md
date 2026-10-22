## 🌱 EcoTrack – Carbon Footprint Web App

EcoTrack is a full-stack web application that helps users track and analyze their carbon footprint. The app allows users to register, log in, input their activities, and view their carbon usage results. It is built using Flask, Python, HTML, and CSS with secure environment configuration.

---

## 🚀 Features

✔ User registration and login  
✔ Track daily carbon footprint activities  
✔ View personalized results and recommendations  
✔ Responsive UI design  
✔ Secure configuration using environment variables

---

## 🛠 Technology Stack

- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS  
- **Templates**: Jinja2  
- **Environment Config**: `.env` file for secrets

---

## 📂 Project Structure

```
carbon_footprint_web_app/
├── .env.example            # Environment configuration template
├── .gitignore              # Git ignore rules
├── app.py                  # Flask application
├── static/
│   └── style.css            # Styling files
├── templates/
│   ├── index.html          # Homepage
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── result.html         # Results page
```

---

## ⚙ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Paulson-2004/EcoTrack-carbon_footprint_web_app.git
   cd carbon_footprint_web_app
   ```

2. Install dependencies:
   ```bash
   pip install flask python-dotenv
   ```

3. Create a `.env` file (copy `.env.example` and set your credentials):
   ```env
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_SERVER=your_db_server
   DB_DATABASE=your_db_database
   DB_PORT=1433
   TRUST_SERVER_CERTIFICATE=true
   SECRET_KEY=your_secret_key
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

---

## 📸 Screenshots

Login/Register Page
<img width="1920" height="879" alt="Screenshot 2025-05-07 214434" src="https://github.com/user-attachments/assets/8a511b2e-6f26-40cb-a94c-ffae3e3579fa" />
Main Page
<img width="1920" height="892" alt="image" src="https://github.com/user-attachments/assets/05e81942-46b6-4994-b53f-66798435cd64" />
Report
<img width="1920" height="881" alt="image" src="https://github.com/user-attachments/assets/9202cd57-8790-4cfd-b639-1d9bbd909abb" />
Database (SSMS)
<img width="1591" height="813" alt="image" src="https://github.com/user-attachments/assets/2afea549-5939-44c8-bd8a-bf1a6eed7041" />

---

## 📞 Contact

Created by **Paulson J.**  
Feel free to fork, contribute, or open issues!

---

**Let’s build a sustainable future, one step at a time! 🌍💚**
