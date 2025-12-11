from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ---------- API LAYER ----------

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    return r.json()

# ---------- ANALYSIS LAYER ----------

def analyze_repos(repos):
    if not repos:
        return {
            "total_repos": 0,
            "total_stars": 0,
            "languages": {},
            "top_repos": []
        }

    languages = {}
    total_stars = 0

    for repo in repos:
        lang = repo.get("language") or "Other"
        languages[lang] = languages.get(lang, 0) + 1
        total_stars += repo.get("stargazers_count", 0)

    # Top 5 repos by stars
    top_repos = sorted(
        repos,
        key=lambda r: r.get("stargazers_count", 0),
        reverse=True
    )[:5]

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "languages": languages,
        "top_repos": top_repos
    }

# ---------- ROUTES / VIEWS ----------

@app.route("/", methods=["GET", "POST"])
def index():
    context = {
        "profile": None,
        "analysis": None,
        "error": None
    }

    if request.method == "POST":
        username = request.form.get("username", "").strip()

        if not username:
            context["error"] = "Please enter a GitHub username."
            return render_template("index.html", **context)

        profile = get_github_profile(username)
        if not profile:
            context["error"] = f"No GitHub user found with username '{username}'."
            return render_template("index.html", **context)

        repos = get_github_repos(username)
        analysis = analyze_repos(repos)

        context["profile"] = profile
        context["analysis"] = analysis

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
