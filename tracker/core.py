
import datetime
from .storage import load_data, save_data

def add_habit(name):
    data = load_data()
    if name in data:
        print(f"Habit '{name}' already exists.")
        return
    data[name] = {
        "created": str(datetime.date.today()),
        "log": []
    }
    save_data(data)
    print(f"Habit '{name}' added.")

def mark_done(name):
    data = load_data()
    if name not in data:
        print(f"Habit '{name}' does not exist.")
        return
    today = str(datetime.date.today())
    if today not in data[name]["log"]:
        data[name]["log"].append(today)
        save_data(data)
        print(f"Habit '{name}' marked as done today.")
    else:
        print(f"Habit '{name}' already marked done today.")

def list_habits():
    data = load_data()
    if not data:
        print("No habits found.")
        return
    today = str(datetime.date.today())
    for name, info in data.items():
        status = "✅" if today in info["log"] else "❌"
        print(f"{name}: {status}")

def show_stats():
    data = load_data()
    if not data:
        print("No habits found.")
        return
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    for name, info in data.items():
        count = sum(1 for date in info["log"] if datetime.date.fromisoformat(date) >= week_ago)
        print(f"{name}: {count} times in the last 7 days")

def reset_week():
    data = load_data()
    for habit in data.values():
        habit["log"] = []
    save_data(data)
    print("All habits have been reset for the new week.")
