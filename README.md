# ⏰ CronCraft (`croncraft`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![Cron Syntax](https://img.shields.io/badge/Crontab-Natural%20Language-yellow.svg)](https://github.com/MochErik/croncraft)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange.svg)](https://github.com/MochErik/croncraft)

> **Human English to Cron Translator & Schedule Explainer CLI.** Translates natural English phrases into standard 5-part crontab expressions and decodes cryptic crontab syntax into crystal-clear human explanations.

---

## 🚀 Quick Install

```bash
pip install croncraft
```

---

## 🖥️ Usage

### 1. Convert English to Crontab
```bash
croncraft "every 15 minutes"
# Output: ⏰ Generated Cron: */15 * * * *

croncraft "every day at 3:30pm"
# Output: ⏰ Generated Cron: 30 15 * * *
```

### 2. Decode Cryptic Crontab Syntax
```bash
croncraft "0 0 1,15 * *"
# Output: 📖 Explanation: At 00:00 on day 1,15 of the month.
```

---

## 📜 License

MIT License © 2026 [Moch. Erik Irriansyah](https://github.com/MochErik)
