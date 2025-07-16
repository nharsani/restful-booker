README.md for Pytest-based API test suite that interacts with the Restful Booker API:

✅ README.md

# 🧪 Restful Booker API Test Suite (Pytest)

This repository contains an automated test suite written in **Python** using **Pytest** to interact with the [Restful Booker API](https://restful-booker.herokuapp.com). The suite performs full CRUD operations: creating bookings, updating bookings, retrieving bookings, and deleting bookings.

## 📦 Features

- ✅ GET all booking IDs
- 🆕 Create 3 bookings
- 🔄 Update 2 bookings
- ❌ Delete 1 booking
- 📄 Convert logs to a styled HTML report

## 🧰 Tech Stack

- Python 3.7+
- Pytest
- Requests
- Logging
- HTML for log visualization

## 🚀 Getting Started

### 1. Clone the Repository

```bash
1. Clone the Repository
git clone https://github.com/your-username/restful-booker-tests.git
cd restful-booker-tests

2. Create a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available, simply install:
pip install pytest requests

4. Run the Test Suite
pytest -v test_booking.py

📂 File Structure
pgsql
Copy
Edit
.
├── test_booking.py       # Main test file
├── api_response.log      # Auto-generated log file
├── api_response.html     # HTML version of the log
└── README.md             # Project documentation

🧪 Test Scenarios
Test Name	Description
test_get_all_bookings	Retrieves all booking IDs
test_updates_2_bookings	Updates total price of two bookings
test_deletes_1_booking	Deletes one of the created bookings
test_convert_logs_to_html	Converts api_response.log to HTML report

🔒 Authentication
Some operations (update/delete) require a token. The suite authenticates using:

json
Copy
Edit
{
  "username": "admin",
  "password": "password123"
}

🧹 Cleanup
After tests run, created bookings are automatically deleted to keep the environment clean.

📝 Logs
All test responses and actions are logged in api_response.log

A styled HTML version of the log is generated as api_response.html

📄 Example HTML Log Output
Logs are styled and presented in an HTML table:

html

<tr class="info">
  <td class="timestamp">2025-07-15 10:01:00</td>
  <td>INFO</td>
  <td>Booking 1 created with ID: 123</td>
</tr>

📧 Contact
For questions or improvements, please open an issue or submit a pull request.
Email: nharsani@yahoo.in

✅ Happy Testing!

Happy Testing

---

✅ requirements.txt

pytest>=7.0
requests>=2.25.1



