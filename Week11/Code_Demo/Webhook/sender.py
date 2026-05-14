import requests
import json
import time

WEBHOOK_URL = 'http://localhost:5001/webhook'

def send_notification_webhook(event_type, payload):
    data = {
        "event": event_type,
        "payload": payload,
        "timestamp": time.time()
    }
    headers = {'Content-Type': 'application/json'}
    
    print(f"Sending webhook for event: {event_type}...")
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print(f"Webhook delivered successfully. Response: {response.json()}")
        else:
            print(f"Webhook delivery failed with status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook: {e}")

if __name__ == '__main__':
    print("Webhook Sender Application")
    print("--------------------------")
    time.sleep(1) # simulate some work
    
    # Simulate a user signup event
    send_notification_webhook("user.signup", {
        "user_id": "1001",
        "username": "new_user",
        "email": "user@example.com"
    })
    
    time.sleep(2)
    
    # Simulate a system alert event
    send_notification_webhook("system.alert", {
        "severity": "high",
        "message": "Disk space usage exceeded 90%"
    })
