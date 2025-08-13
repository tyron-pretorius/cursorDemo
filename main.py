"""
Lesson 4: Debugging demo

Use this script to practice:
- Setting breakpoints in PyCharm
- Stepping through code
- Inspecting variables
- Copying error messages into an LLM to get help
"""

from datetime import datetime

# Small in-memory dataset
opportunities = [
    {"id": "OPP-1001", "mql_date": "2024-01-15", "close_date": "2024-02-10", "amount_usd": 5400,  "stage": "Closed Won"},
    {"id": "OPP-1002", "mql_date": "2024-01-20", "close_date": "2024-03-05", "amount_usd": 12000, "stage": "Closed Won"},
    {"id": "OPP-1003", "mql_date": "2024-02-01", "close_date": "2024-02-25", "amount_usd": 7500,  "stage": "Closed Lost"},
    {"id": "OPP-1004", "mql_date": "2024-02-10", "close_date": "2024-03-15", "amount_usd": 9800,  "stage": "Closed Won"},
]

def days_between(a: str, b: str) -> int:
    fmt = "%Y-%m-%d"
    return (datetime.strptime(b, fmt) - datetime.strptime(a, fmt)).days

def step1_sum_amounts(rows):
    print("\n[STEP 1] Summing deal amounts (USD)")
    total = 0
    for i, opp in enumerate(rows):
        total += opp["amount_usd"]   # Bug #1: one value is a string → TypeError
    print(f"Total revenue: {total}")
    return total

def step2_each_velocity(rows):
    print("\n[STEP 2] Velocity per opportunity (days from MQL to Close)")
    velocities = []
    for i in range(len(rows)):
        r = rows[i]
        v = days_between(r["mql_date"], r["close_date"])  # Bug #2: fixed wrong key 'mqlDate' → KeyError
        velocities.append(v)
    print(f"Velocities: {velocities}")
    return velocities

def step3_average_closed_won(rows):
    print("\n[STEP 3] Average velocity for Closed Won only")
    closed_won = []
    for r in rows:
        if r.get("stage") == "Closed Won":  # Bug #3: fixed should be 'stage' → list stays empty
            v = days_between(r["mql_date"], r["close_date"])
            closed_won.append(v)
    avg_velocity = sum(closed_won) / len(closed_won)  # divide by zero if list is empty
    print(f"Average velocity (Closed Won): {avg_velocity} days")
    return avg_velocity

def main():
    print("[INFO] Starting Lesson 4 debugging demo…")
    total = step1_sum_amounts(opportunities)
    per_opp = step2_each_velocity(opportunities)
    avg_won = step3_average_closed_won(opportunities)
    print("\nAll steps completed successfully!", total, per_opp, avg_won)

if __name__ == "__main__":
    main()