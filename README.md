API Testing Script for Restful Booker
Overview
This Python script is designed to test various API endpoints of the Restful Booker service. It includes functions for performing CRUD operations (Create, Read, Update, Delete) and logs all the interactions into a log file. At the end, the log is converted into an HTML file for easy review.

The script makes use of the following API actions:

GET: Retrieve all bookings.

POST: Create new bookings.

PATCH: Update booking details.

DELETE: Delete a booking.

It logs the details of each API request and response and generates an HTML report for easier analysis.

Prerequisites
Python 3.x

Required Python Libraries:

requests

json

logging

os

Install Required Libraries
To install the required libraries, run the following command:

bash
Copy
Edit
pip install requests
Script Details
Functions
test_get_all_bookings():

Sends a GET request to retrieve all booking IDs.

Logs the response status and data.

test_create_3_bookings():

Sends POST requests to create 3 new bookings.

Logs the response for each booking creation.

Returns the booking IDs for further updates and deletions.

test_updates_2_bookings(bookingid1, price1, bookingid2, price2):

Sends PATCH requests to update the prices of two bookings (given their IDs).

Requires authentication (username and password).

Logs the response for each booking update.

test_deletes_1_booking(bookingid):

Sends a DELETE request to remove a booking by ID.

Logs the deletion status and response.

convert_logs_to_html():

Converts the api_response.log file to an HTML file (api_response.html).

Formats the log entries as an HTML table with styling for easy reading.

Differentiates log levels with color (INFO in green, ERROR in red).

Example Usage
To run the script:

Run the Script:

This will execute all the tests sequentially (GET, POST, PATCH, DELETE) and generate the HTML log.

bash
Copy
Edit
python api_test_script.py
Generated Files:

api_response.log: A plain text file containing the log entries for each API request and response.

api_response.html: A human-readable HTML version of the log file, formatted as a table with timestamps, log levels, and messages.

Example Output
Console Output: The script prints the status of each API request to the console. For example:

csharp
Copy
Edit
All booking IDs retrieved successfully:
[{ "bookingid": 1, "firstname": "John", ... }]
Successfully created first booking with ID: 12345
Successfully updated first booking with ID: 12345
Successfully deleted booking with ID: 12345
Log File (api_response.log): The log file will contain entries like:

yaml
Copy
Edit
2025-07-15 12:34:56,789 - INFO - Get Request Status Code: 200
2025-07-15 12:34:57,890 - INFO - First Booking Done with Status Code: 200
2025-07-15 12:35:01,123 - ERROR - Booking ID 12345 Deleted with Status Code: 404
HTML Log (api_response.html): The HTML file will have a table like this:

html
Copy
Edit
<html>
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
            <tr><th>Timestamp</th><th>Log Level</th><th>Message</th></tr>
            <tr class="info">
                <td class="timestamp">2025-07-15 12:34:56</td>
                <td>INFO</td>
                <td>Get Request Status Code: 200</td>
            </tr>
            <tr class="error">
                <td class="timestamp">2025-07-15 12:35:01</td>
                <td>ERROR</td>
                <td>Booking ID 12345 Deleted with Status Code: 404</td>
            </tr>
        </table>
    </body>
</html>
Troubleshooting
Authentication Issues:

Ensure that you are using the correct credentials (username and password) for the auth API endpoint.

API Rate Limits:

If the server is slow or unresponsive, check for rate limits or ensure the service is up.

File Permissions:

Ensure that the script has the necessary permissions to write to the log and HTML files (api_response.log and api_response.html).

License
This project is licensed under the MIT License - see the LICENSE file for details.

End of README
This README file covers the following:

Purpose of the script.

Installation and setup.

Explanation of each function.

How to run the script and interpret the output.

Troubleshooting common issues.
