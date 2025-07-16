`README.md` for API testing script test_booking.py

---

### 📄 README.md

# 🧪 Restful Booker API Testing Script

## 📌 Overview

This Python-based test suite is designed to validate various endpoints of the **[Restful Booker API](https://restful-booker.herokuapp.com)**. It performs full **CRUD operations** (Create, Read, Update, Delete), logs all interactions, and generates a styled **HTML log report** for easier review and analysis.

---

## 🔧 Features

* ✅ **GET**: Retrieve all booking IDs
* 🆕 **POST**: Create new bookings
* ✏️ **PATCH**: Update booking details
* ❌ **DELETE**: Delete bookings
* 📄 **Logging**: Logs each request and response
* 🌐 **HTML Report**: Converts logs to a formatted HTML file (`api_response.html`)

---

## 📥 Prerequisites

* Python **3.x** installed

### Required Python Libraries

* `requests`
* `json` *(standard library)*
* `logging` *(standard library)*
* `os` *(standard library)*

---

## 📦 Installation

To install the required libraries, run:

```bash
pip install requests
```

> Note: `json`, `logging`, and `os` are built-in and do not require separate installation.

---

## 📂 Script Overview

### 🔍 Test Functions

#### `test_get_all_bookings()`

* Sends a **GET** request to retrieve all booking IDs.
* Logs the response status and content.

#### `test_create_3_bookings()`

* Sends **POST** requests to create 3 bookings.
* Logs each booking's response and stores their IDs for further use.

#### `test_updates_2_bookings(bookingid1, price1, bookingid2, price2)`

* Sends **PATCH** requests to update prices of two bookings.
* Requires authentication.
* Logs response and success status.

#### `test_deletes_1_booking(bookingid)`

* Sends a **DELETE** request to remove a booking by ID.
* Logs the result of the operation.

#### `test_convert_logs_to_html()`

* Converts the plain-text log file `api_response.log` into a styled HTML file `api_response.html`.
* Differentiates log levels (INFO in green, ERROR in red).

---

## ▶️ Running the Script

Use `python` to run the test suite:

```bash
python test_get_all_bookings.py
```

This will:

1. Perform all API operations.
2. Log responses in `api_response.log`.
3. Convert the log into `api_response.html` for easier visualization.

---

## 📁 Generated Files

* `api_response.log`: Raw text log of each API request and response.
* `api_response.html`: Styled HTML version of the log.
* `test_booking.py`: Main test script.

---

## 📤 Sample Console Output

```bash
All booking IDs retrieved: [{"bookingid": 1, "firstname": "Naveen", ...}]
Successfully created first booking with ID: 12345
Successfully updated first booking with ID: 12345
Successfully deleted booking with ID: 12345
```

---

## 📄 Sample Log Entry (`api_response.log`)

```
2025-07-15 12:34:56,789 - INFO - Get Request Status Code: 200
2025-07-15 12:35:01,123 - INFO - Booking 1 created with ID: 12345
2025-07-15 12:35:10,456 - ERROR - Booking update failed with Status Code: 500
```

---

## 🌐 Sample HTML Output (`api_response.html`)

```html
<tr class="info">
  <td class="timestamp">2025-07-15 12:34:56</td>
  <td>INFO</td>
  <td>Get Request Status Code: 200</td>
</tr>
<tr class="error">
  <td class="timestamp">2025-07-15 12:35:10</td>
  <td>ERROR</td>
  <td>Booking update failed with Status Code: 500</td>
</tr>
```

---

## 🛠️ Troubleshooting

### ✅ Authentication Issues

* Ensure you're using valid credentials:

  ```json
  {
    "username": "admin",
    "password": "password123"
  }
  ```

### 🔁 API Rate Limits or Downtime

* The Heroku API may be temporarily down or rate-limited. Retry after a short wait.

### 🔒 File Permission Errors

* Make sure your script has write access to create `api_response.log` and `api_response.html`.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📚 Summary

* ✅ A Pytest-based automated API testing framework
* 🎯 Designed to work with the public Restful Booker API
* 📈 Generates both text and HTML log reports
* 💡 Easily customizable for other APIs

---

🔚 **End of README**


