"""CronCraft CLI Main Entrypoint."""

import argparse
import sys
from typing import List

from croncraft.translator import natural_to_cron
from croncraft.explainer import explain_cron

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"


def main(args: List[str] = None):
    parser = argparse.ArgumentParser(
        prog="croncraft",
        description="⏰ CronCraft - Human English to Cron Translator & Schedule Explainer CLI",
        epilog="Examples:\n"
               "  croncraft \"every 15 minutes\"     # Output: */15 * * * *\n"
               "  croncraft \"every day at 3:30pm\"   # Output: 30 15 * * *\n"
               "  croncraft parse \"0 0 1 * *\"       # Decode crontab expression\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("input", help="Natural English phrase or cron expression to parse")
    parser.add_argument("--parse", "-p", action="store_true", help="Parse and explain existing cron expression")

    parsed = parser.parse_args(args)
    text = parsed.input.strip()

    # If it looks like a cron (5 space separated tokens) or flag given
    if parsed.parse or len(text.split()) == 5:
        res = explain_cron(text)
        if res.get("valid"):
            print(f"\n{CYAN}{BOLD}⏰ Crontab Expression:{RESET} {GREEN}{BOLD}{res['cron']}{RESET}")
            print(f"📖 {BOLD}Explanation:{RESET} {res['description']}")
            print(f"{DIM}Breakdown: Min={res['breakdown']['minute']}, Hour={res['breakdown']['hour']}, Day={res['breakdown']['day_of_month']}, Month={res['breakdown']['month']}, Weekday={res['breakdown']['day_of_week']}{RESET}\n")
        else:
            print(f"{YELLOW}❌ {res.get('description')}{RESET}")
    else:
        res = natural_to_cron(text)
        print(f"\n{CYAN}{BOLD}📝 Human Request:{RESET} \"{text}\"")
        print(f"⏰ {BOLD}Generated Cron:{RESET} {GREEN}{BOLD}{res['cron']}{RESET}")
        print(f"📖 {DIM}{res['desc']}{RESET}\n")


if __name__ == "__main__":
    main()
