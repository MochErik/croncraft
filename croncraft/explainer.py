"""Crontab expression decoder and timeline simulator."""

import datetime
from typing import Dict, Any, List

DAY_MAP = {
    "0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday",
    "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"
}

MONTH_MAP = {
    "1": "January", "2": "February", "3": "March", "4": "April",
    "5": "May", "6": "June", "7": "July", "8": "August",
    "9": "September", "10": "October", "11": "November", "12": "December"
}


def explain_cron(cron_str: str) -> Dict[str, Any]:
    """Break down a 5-part crontab expression into human description."""
    parts = cron_str.strip().split()
    if len(parts) != 5:
        return {"valid": False, "description": "Invalid crontab format. Must have exactly 5 parts."}

    m, h, dom, mon, dow = parts[0], parts[1], parts[2], parts[3], parts[4]

    # Description generation
    time_desc = ""
    if m.startswith("*/"):
        time_desc = f"Every {m[2:]} minutes"
    elif m == "*" and h == "*":
        time_desc = "Every minute"
    elif m != "*" and h == "*":
        time_desc = f"At minute {m} of every hour"
    elif m != "*" and h != "*":
        time_desc = f"At {int(h):02d}:{int(m):02d}"

    day_desc = ""
    if dow != "*":
        days = [DAY_MAP.get(d, d) for d in dow.split(",")]
        day_desc = f" on {', '.join(days)}"

    date_desc = ""
    if dom != "*":
        date_desc = f" on day {dom} of the month"

    month_desc = ""
    if mon != "*":
        months = [MONTH_MAP.get(m, m) for m in mon.split(",")]
        month_desc = f" in {', '.join(months)}"

    full_desc = f"{time_desc}{day_desc}{date_desc}{month_desc}."

    return {
        "valid": True,
        "cron": cron_str,
        "description": full_desc.strip(),
        "breakdown": {
            "minute": m,
            "hour": h,
            "day_of_month": dom,
            "month": mon,
            "day_of_week": dow
        }
    }
