# Python Datadog Monitoring Automation

This project automates monitoring checks using the Datadog API. A lightweight Python script to check the status of your Datadog monitors and log the results. Ideal for running as a scheduled job via cron or CI/CD pipelines.

---

##  Project Structure

```bash
python-datadog-monitoring-automation/
├── config/
│   └── secrets.yaml          # Stores API keys and Slack webhook
├── scripts/
│   └── monitor_checker.py    # Main monitoring script
├── logs/
│   └── execution.log         # Optional log file
├── README.md
└── requirements.txt
```

## Features
- Authenticates with the Datadog API using keys stored in secrets.yaml

- Queries and filters monitors based on status (e.g., Alert, Warn)

- Sends alert summaries to a Slack channel

- Logs results to a file for historical tracking

- Designed for standalone execution or scheduled automation via cron

## Requirements
Install dependencies using pip:

```bash
pip install -r requirements.txt
```
## Python version
- Python 3.8 or later is recommended

##  Configuration
- Create a `config/secrets.yaml` file with your Datadog API keys and Slack webhook URL.

 > Keep this file secure. Never commit it to a public repo. You can use .gitignore to ignore this file.

## Usage
Run the script directly:

```bash
python scripts/monitor_checker.py
```
## Scheduling with cron (Automation)
To run this script periodically, you can set up a cron job. For example, to run it every hour:

```bash
# Open crontab
crontab -e

# Example: Run every hour
0 * * * * /usr/bin/python3 /full/path/to/scripts/monitor_checker.py >> /full/path/to/logs/execution.log 2>&1
```
> Make sure to use the full path to both Python and the script.
## Logging
- The script can log its execution results to `logs/execution.log`. All execution details and errors are saved to this file.
- This is optional but recommended for tracking historical data. This helps with debugging and reviewing historical runs.


## Sample Output

```bash
[INFO] Loaded environment variables.
[INFO] Checked 10 monitors.
[OK] All monitors are OK.
```

- or in case of failed monitors:
```bash
[WARNING] 3 monitor(s) are in failed state!
Monitor: High CPU on Production
Monitor: API Gateway Latency Alert
Monitor: DB Replication Lag
```

## Results : Slack Notifications
- The script formats messages and posts summaries of triggered Datadog monitors directly to a Slack channel via the configured webhook.

- Example Slack message:
```bash
 Datadog Monitor Alert
 monitor-name-1 — ALERT
 monitor-name-2 — WARN
 monitor-name-3 — ALERT
```