# app.py
from src.dashboard import create_dashboard

if __name__ == "__main__":
    app = create_dashboard()
    print("Dashboard running: http://127.0.0.1:8050")
    app.run(debug=True)