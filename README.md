⭐ GitHub Profile Analyser

GitHub Profile Analyser is a Flask-based web application that fetches and analyzes any GitHub user’s public profile using the GitHub REST API. It generates a recruiter-friendly summary showing top repositories, language usage, total stars, and profile activity — making it easy to evaluate a developer at a glance.

 Features

- Search any GitHub username

- View detailed profile info (bio, followers, following, avatar, etc.)

- Analyze repositories (stars, languages, total repos)

 Automatic insights like:

1.Most used languages

2.Top 5 repositories

3.Total star count

🎨 Clean UI for a recruiter-style profile view

⚡ Powered by Flask + GitHub REST API

Tech Stack

Python

Flask

GitHub REST API

HTML / CSS

Requests library

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/jothyshivani145/Github-profile-Analyser.git
cd Github-profile-Analyser

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment

Windows CMD:

venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open your browser and go to:

http://127.0.0.1:5000

🛠️ How It Works

User enters a GitHub username.

Flask sends a request to GitHub’s API.

The app retrieves:

Repositories

Stars

Languages

Profile details

The data is analyzed and displayed in a clean, organized dashboard.

🤝 Contributing

Pull requests are welcome!
If you’d like to improve the UI or add features like charts, feel free to open an issue.

📜 License

This project is open-source under the MIT license.
