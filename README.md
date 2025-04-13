# Elke: Basic Equipment Health Monitoring in Python 🛠️📊

Elke is a simple Python project that simulates the monitoring of temperature and vibration in machines. It generates random values, checks for abnormal conditions, and logs the data into a CSV file. This project is perfect for beginners who want to practice Python with a real-world use case.

---

## 🚀 Features

- Simulates temperature and vibration readings
- Displays real-time alerts if limits are exceeded
- Logs all data with timestamps into a CSV file
- Easy to run and understand

---

## 🧰 Technologies Used

- Python 3
- `random` – to generate simulated data
- `csv` – for data logging
- `time` – to simulate real-time data flow

---

## 🛠️ How It Works

1. The program runs a loop to simulate 10 sensor readings.
2. Each loop generates random temperature (30-70°C) and vibration (40-90 units) values.
3. If the values exceed safe limits (Temp > 50°C, Vibration > 70 units), it prints an alert.
4. All readings are saved in a file called `elke_log.csv`.

---

## 📂 Output Example

```text
[1] Temp: 45°C | Vibration: 65 | Status: Normal
[2] Temp: 55°C | Vibration: 75 | Status: ⚠ Alert: Check Machine!
...
