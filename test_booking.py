import pytest
import requests
import json
import logging
import os

BASE_URL = "https://restful-booker.herokuapp.com"
HTML_LOG_FILE = 'api_response.html'

# Logging setup
logging.basicConfig(
    filename='api_response.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fixture to create bookings
@pytest.fixture(scope='module')
def created_bookings():
    headers = {"Content-Type": "application/json"}
    payloads = [
        {
            "firstname": "Naveen",
            "lastname": "Harsani",
            "totalprice": 1111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-7-15",
                "checkout": "2025-7-16"
            },
            "additionalneeds": "Lunch"
        },
        {
            "firstname": "Rajesh",
            "lastname": "Kulkarni",
            "totalprice": 2222,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-8-15",
                "checkout": "2025-8-16"
            },
            "additionalneeds": "Breakfast"
        },
        {
            "firstname": "Dinesh",
            "lastname": "Maharaja",
            "totalprice": 3333,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-9-15",
                "checkout": "2025-9-16"
            },
            "additionalneeds": "Dinner"
        }
    ]

    booking_ids = []
    for i, payload in enumerate(payloads):
        response = requests.post(f"{BASE_URL}/booking", headers=headers, data=json.dumps(payload))
        assert response.status_code == 200
        booking_id = response.json()["bookingid"]
        logging.info(f"Booking {i+1} created with ID: {booking_id}")
        booking_ids.append(booking_id)

    yield booking_ids

    # Cleanup after tests
    token = get_auth_token()
    headers["Cookie"] = f"token={token}"
    for bid in booking_ids:
        requests.delete(f"{BASE_URL}/booking/{bid}", headers=headers)
        logging.info(f"Booking {bid} deleted in cleanup")

# Fixture for auth token
@pytest.fixture(scope="module")
def auth_headers():
    token = get_auth_token()
    return {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

# Helper function for auth
def get_auth_token():
    credentials = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", data=credentials)
    assert response.status_code == 200
    return response.json()["token"]

# Test: GET all bookings
def test_get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    logging.info("All booking IDs retrieved.")
    print("All booking IDs retrieved:", response.json())

# Test: Update 2 bookings
def test_updates_2_bookings(created_bookings, auth_headers):
    bookingid1, bookingid2 = created_bookings[0], created_bookings[1]

    update1 = {"totalprice": 1000}
    update2 = {"totalprice": 1500}

    response1 = requests.patch(f"{BASE_URL}/booking/{bookingid1}", headers=auth_headers, data=json.dumps(update1))
    response2 = requests.patch(f"{BASE_URL}/booking/{bookingid2}", headers=auth_headers, data=json.dumps(update2))

    assert response1.status_code == 200
    assert response2.status_code == 200

    logging.info(f"Updated booking {bookingid1} with new price {update1['totalprice']}")
    logging.info(f"Updated booking {bookingid2} with new price {update2['totalprice']}")

# Test: Delete 1 booking
def test_deletes_1_booking(created_bookings, auth_headers):
    bookingid = created_bookings[0]
    response = requests.delete(f"{BASE_URL}/booking/{bookingid}", headers=auth_headers)
    assert response.status_code == 201
    logging.info(f"Deleted booking {bookingid}")
    print(f"Deleted booking {bookingid}")

# Final test: Convert logs to HTML
def test_convert_logs_to_html():
    if os.path.exists('api_response.log'):
        with open('api_response.log', 'r') as log_file:
            log_content = log_file.readlines()

        html_content = '''<html>
            <head>
                <title>API Response Log</title>
                <style>
                    body { font-family: Arial; background-color: #f4f4f4; }
                    table { width: 100%; border-collapse: collapse; }
                    th, td { padding: 10px; border: 1px solid #ddd; }
                    th { background-color: #f2f2f2; }
                    .info { color: green; }
                    .error { color: red; }
                    .timestamp { font-size: 0.9em; color: #aaa; }
                </style>
            </head>
            <body>
                <h2>API Response Log</h2>
                <table>
                    <tr><th>Timestamp</th><th>Log Level</th><th>Message</th></tr>'''

        for line in log_content:
            timestamp, level, message = line.split(' - ', 2)
            row_class = 'info' if level.strip() == 'INFO' else 'error'
            html_content += f'''
                <tr class="{row_class}">
                    <td class="timestamp">{timestamp}</td>
                    <td>{level}</td>
                    <td>{message}</td>
                </tr>'''

        html_content += '''
                </table>
            </body>
            </html>'''

        with open(HTML_LOG_FILE, 'w') as html_file:
            html_file.write(html_content)

        logging.info(f"Log has been converted to HTML and saved as {HTML_LOG_FILE}")
