# Main monitoring script

import yaml
import requests
from datadog import initialize, api


# Load secrets from YAML
def load_secrets(path="config/secrets.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)


# Initialize Datadog API
def init_datadog(api_key, app_key):
    options = {
        "api_key": api_key,
        "app_key": app_key,
    }
    initialize(**options)


# Get all monitor states
def get_failing_monitors():
    monitors = api.Monitor.get_all()
    failing = []
    for monitor in monitors:
        if monitor.get("overall_state") in ("Alert", "Warn"):
            failing.append(monitor)
    return failing


# Send message to Slack
def send_to_slack(webhook_url, monitors):
    if not monitors:
        return  # No issues, no alert

    text_lines = [" *Datadog Monitor Alert!*"]
    for m in monitors:
        line = f"- *{m['name']}* is in state: `{m['overall_state']}`"
        text_lines.append(line)

    payload = {"text": "\n".join(text_lines)}

    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f"Slack error: {response.status_code} - {response.text}")


# Main logic
def main():
    secrets = load_secrets()
    init_datadog(
        api_key=secrets["datadog"]["api_key"], app_key=secrets["datadog"]["app_key"]
    )
    monitors = get_failing_monitors()
    send_to_slack(secrets["slack"]["webhook_url"], monitors)


if __name__ == "__main__":
    main()
