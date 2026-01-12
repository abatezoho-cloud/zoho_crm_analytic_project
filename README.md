# Zoho Analytics to Zoho CRM Automation (Python)

This project automatically fetches data from **Zoho Analytics** tables and pushes it into **Zoho CRM modules** using APIs.  
It is designed to run **without any frontend**, deployed on a server (DigitalOcean), and scheduled to execute at a fixed time every day **except Monday**.

---

## 🚀 What This Project Does

1. Generates and manages **Zoho OAuth access tokens**
2. Fetches data from:
   - Keratoconus Analytics View
   - Vision Therapy Analytics View
3. Saves raw analytics data as JSON (for backup/debugging)
4. Transforms analytics data into CRM-compatible format
5. Pushes records to Zoho CRM module in **batch mode**
6. Can be scheduled using **cron jobs**

---

## 📂 Project Structure

├── main.py
├── get_data_from_anlytics.py
├── token_gen.py
├── transform.py
├── push_to_crm.py
├── config.py
├── .env
├── data/
│ ├── token/
│ │ └── access_token.json
│ └── analyst_data/
│ ├── analytics_data_keratoconus.json
│ └── analytics_data_vision_therapy.json

## 🧠 File-by-File Explanation

### `main.py`
- Entry point of the project
- Fetches analytics data
- Transforms it
- Pushes it to Zoho CRM

---

### `get_data_from_anlytics.py`
- Fetches data from Zoho Analytics REST API
- Saves response as JSON
- Returns analytics rows as Python list

Functions:
- `analytics_data_keratoconus()`
- `analytics_data_vision_therapy()`

---

### `token_gen.py`
- Handles Zoho OAuth token lifecycle
- Uses refresh token to generate access token
- Stores token with expiry time in JSON
- Automatically refreshes expired tokens

---

### `config.py`
- Loads environment variables using **Pydantic**
- Keeps credentials secure

---

### `transform.py`
- Converts analytics data into CRM-ready format
- Formats dates into ISO format
- Adds custom fields like `Category` and `Branch`

Functions:
- `tranform_kera()`
- `tranform_visthe()`

---

### `push_to_crm.py`
- Pushes data to Zoho CRM module
- Sends data in batches (default 100 records)
- Prevents API limit issues

---

## 🔐 Environment Variables (`.env`)

Create a `.env` file in the project root:

zoho_client_id=YOUR_CLIENT_ID
zoho_client_secret=YOUR_CLIENT_SECRET
zoho_refresh_token=YOUR_REFRESH_TOKEN

⚠️ **Never commit `.env` to GitHub**

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/zoho-analytics-crm.git
cd zoho-analytics-crm