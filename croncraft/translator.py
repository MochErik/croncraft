"""Natural English to 5-part standard Cron expression translator."""

import re
from typing import Optional, Dict, Any


def natural_to_cron(phrase: str) -> Dict[str, Any]:
    """Parse common human language phrases into standard 5-column crontab expression."""
    p = phrase.lower().strip()

    # Pre-canned patterns
    if "every minute" in p:
        return {"cron": "* * * * *", "desc": "Every minute"}
    if "every 5 minutes" in p:
        return {"cron": "*/5 * * * *", "desc": "Every 5 minutes"}
    if "every 10 minutes" in p:
        return {"cron": "*/10 * * * *", "desc": "Every 10 minutes"}
    if "every 15 minutes" in p:
        return {"cron": "*/15 * * * *", "desc": "Every 15 minutes"}
    if "every 30 minutes" in p or "every half hour" in p:
        return {"cron": "*/30 * * * *", "desc": "Every 30 minutes"}
    if "every hour" in p or "hourly" in p:
        return {"cron": "0 * * * *", "desc": "Every hour at minute 0"}
    if "every day at midnight" in p or "midnight" in p:
        return {"cron": "0 0 * * *", "desc": "At midnight (00:00) every day"}
    if "every day at noon" in p or "noon" in p:
        return {"cron": "0 12 * * *", "desc": "At noon (12:00) every day"}
    if "every day at" in p:
        # e.g. every day at 3am or 3:30pm
        time_match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", p)
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            meridiem = time_match.group(3)
            if meridiem == "pm" and hour < 12:
                hour += 12
            elif meridiem == "am" and hour == 12:
                hour = 0
            return {"cron": f"{minute} {hour} * * *", "desc": f"Every day at {hour:02d}:{minute:02d}"}
    if "every monday" in p or "on monday" in p:
        return {"cron": "0 9 * * 1", "desc": "Every Monday at 09:00"}
    if "every friday" in p or "on friday" in p:
        return {"cron": "0 17 * * 5", "desc": "Every Friday at 17:00"}
    if "weekdays" in p:
        return {"cron": "0 9 * * 1-5", "desc": "Monday through Friday at 09:00"}
    if "weekends" in p:
        return {"cron": "0 10 * * 6,0", "desc": "Saturday and Sunday at 10:00"}
    if "every month" in p or "monthly" in p:
        return {"cron": "0 0 1 * *", "desc": "First day of every month at midnight"}

    # Fallback to daily midnight
    return {"cron": "0 0 * * *", "desc": f"Interpreted as daily midnight for '{phrase}'"}
