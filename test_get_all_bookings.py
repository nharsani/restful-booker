import requests
import json
import logging
import os

BASE_URL = "https://restful-booker.herokuapp.com"
HTML_LOG_FILE = 'api_response.html'

logging.basicConfig(
    filename='api_response.log',  # Log file name
    level=logging.INFO,           # Set the log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def test_get_all_bookings():
    # API GET request to retrieve all booking IDs
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    print("All booking IDs retrieved successfully:")
    print(response.text)
    logging.info(f"Get Request Status Code: {response.status_code}")
    logging.info(f"Get Request Response Text: {response.text}")


def test_create_3_bookings():
    # Create 3 new bookings using POST API
    payload1 = {
        "firstname": "Naveen",
        "lastname": "Harsani",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-7-15",
            "checkout": "2025-7-16"
        },
        "additionalneeds": "Lunch"
    }
    payload2 = {
        "firstname": "Rajesh",
        "lastname": "Kulkarni",
        "totalprice": 2222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-8-15",
            "checkout": "2025-8-16"
        },
        "additionalneeds": "BreakFast"
    }
    payload3 = {
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
    headers = {
        "Content-Type": "application/json"
    }

    response1 = requests.post(f"{BASE_URL}/booking", headers=headers, data=json.dumps(payload1))
    assert response1.status_code == 200
    response1_json = json.loads(response1.text)
    print(f"Successfully created first booking with ID: {response1_json['bookingid']}")
    logging.info(f"First Booking Done with Status Code: {response1.status_code}")
    logging.info(f"First Booking Done with Response Text: {response1.text}")
    response2 = requests.post(f"{BASE_URL}/booking", headers=headers, data=json.dumps(payload2))
    assert response2.status_code == 200
    response2_json = json.loads(response2.text)
    print(f"Successfully created second booking with ID: {response2_json['bookingid']}")
    logging.info(f"Second Booking Done with Status Code: {response2.status_code}")
    logging.info(f"Second Booking Done with Response Text: {response2.text}")
    response3 = requests.post(f"{BASE_URL}/booking", headers=headers, data=json.dumps(payload3))
    assert response3.status_code == 200
    response3_json = json.loads(response3.text)
    print(f"Successfully created third booking with ID: {response3_json['bookingid']}")
    logging.info(f"Third Booking Done with Status Code: {response3.status_code}")
    logging.info(f"Third Booking Done with Response Text: {response3.text}")
    return response1_json['bookingid'],response2_json['bookingid'],response3_json['bookingid']

def test_updates_2_bookings(bookingid1, price1, bookingid2, price2):
    # Patch API - Updates 2 new bookings which were made in the last step with price1 and price2 respectively
    updated_payload1 = {
        "totalprice": price1
    }

    updated_payload2 = {
        "totalprice": price2
    }

    credentials = {
        "username": "admin",
        "password": "password123"
    }

    auth_response1 = requests.post(f"{BASE_URL}/auth", data=credentials)
    auth_response1_json = auth_response1.json()
    token1 = auth_response1_json.get("token")
    token1_full = f"token={token1}"
    headers1 = {
        "Content-Type": "application/json",
        "Cookie": token1_full
    }

    updated_response1 = requests.patch(f"{BASE_URL}/booking/{bookingid1}", headers=headers1, data=json.dumps(updated_payload1))
    assert updated_response1.status_code == 200
    print(updated_response1.text)
    print(f"Successfully updated first booking with ID: {bookingid1}")
    logging.info(f"First Booking Updated Status Code: {updated_response1.status_code}")
    logging.info(f"First Booking Updated Response Text: {updated_response1.text}")
    auth_response2 = requests.post(f"{BASE_URL}/auth", data=credentials)
    auth_response2_json = auth_response2.json()
    token2 = auth_response2_json.get("token")
    token2_full = f"token={token2}"
    headers2 = {
        "Content-Type": "application/json",
        "Cookie": token2_full
    }


    updated_response2 = requests.patch(f"{BASE_URL}/booking/{bookingid2}", headers=headers2, data=json.dumps(updated_payload2))
    assert updated_response1.status_code == 200
    print(updated_response2.text)
    print(f"Successfully updated second booking with ID: {bookingid2}")
    logging.info(f"Second Booking Updated Status Code: {updated_response2.status_code}")
    logging.info(f"Second Booking Updated Response Text: {updated_response2.text}")


def test_deletes_1_booking(bookingid):
    # deletes 1 booking using DELETE API

    credentials = {
        "username": "admin",
        "password": "password123"
    }

    auth_response = requests.post(f"{BASE_URL}/auth", data=credentials)
    auth_response_json = auth_response.json()
    token3 = auth_response_json.get("token")
    token3_full = f"token={token3}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": token3_full
    }


    delete_response = requests.delete(f"{BASE_URL}/booking/{bookingid}", headers=headers)
    assert delete_response.status_code == 201
    print(f"Successfully deleted booking with ID: {bookingid}")
    logging.info(f"Booking ID {bookingid} Deleted with Status Code: {delete_response.status_code}")

def convert_logs_to_html():
    if os.path.exists('api_response.log'):
        with open('api_response.log', 'r') as log_file:
            log_content = log_file.readlines()

        # Start the HTML file with necessary HTML tags
        html_content = '''<html>
            <head>
                <title>API Response Log</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
                    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
                    th, td { padding: 10px; border: 1px solid #ddd; }
                    th { background-color: #f2f2f2; text-align: left; }
                    .info { color: #4CAF50; }
                    .error { color: #F44336; }
                    .timestamp { font-size: 0.9em; color: #aaa; }
                </style>
            </head>
            <body>
                <h2>API Response Log</h2>
                <table>
                    <tr><th>Timestamp</th><th>Log Level</th><th>Message</th></tr>'''

        # Iterate through the log file and format it in HTML
        for line in log_content:
            timestamp, level, message = line.split(' - ', 2)
            level = level.strip()
            message = message.strip()

            # Adding different styles for INFO and ERROR
            if level == 'INFO':
                row_class = 'info'
            else:
                row_class = 'error'

            # Add each log entry as a row in the table
            html_content += f'''
                    <tr class="{row_class}">
                        <td class="timestamp">{timestamp}</td>
                        <td>{level}</td>
                        <td>{message}</td>
                    </tr>'''

        # Close the table and HTML tags
        html_content += '''
                </table>
            </body>
            </html>'''

        # Write the HTML content to the HTML log file
        with open(HTML_LOG_FILE, 'w') as html_file:
            html_file.write(html_content)

        print(f"Log has been converted to HTML and saved as {HTML_LOG_FILE}")

test_get_all_bookings()
bookingid1, bookingid2, bookingid3 = test_create_3_bookings()
test_updates_2_bookings(bookingid1,1000, bookingid2, 1500)
test_deletes_1_booking(bookingid1)
#test_deletes_1_booking(bookingid2)
convert_logs_to_html()
