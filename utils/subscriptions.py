import pandas as pd

def detect_subscriptions(df):
    # Ensure date is datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Group by merchant/description
    grouped = df.groupby("description")

    subscriptions = []

    for desc, group in grouped:
        group = group.sort_values("date")

        # Calculate gaps between payments
        group["gap"] = group["date"].diff().dt.days

        # Detect recurring patterns
        if group["gap"].median() in [28, 29, 30, 31]:  # monthly
            freq = "Monthly"
        elif group["gap"].median() in [6, 7, 8]:  # weekly
            freq = "Weekly"
        else:
            continue  # not recurring

        subscriptions.append({
            "description": desc,
            "frequency": freq,
            "average_amount": round(group["amount"].mean(), 2),
            "last_payment": group["date"].max().date(),
        })

    return pd.DataFrame(subscriptions)
