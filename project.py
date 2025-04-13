import random
import time
import csv

# Safety limits
MAX_TEMP = 50  # Max temperature in °C
MAX_VIB = 70   # Max vibration level

# Create a CSV file and write the header
with open('elke_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Temperature (°C)', 'Vibration Level', 'Status'])

# Run 10 simulated checks
for i in range(10):
    temp = random.randint(30, 70)  # Simulated temperature
    vib = random.randint(40, 90)   # Simulated vibration
    status = "Normal"

    if temp > MAX_TEMP or vib > MAX_VIB:
        status = "⚠ Alert: Check Machine!"

    print(f"[{i+1}] Temp: {temp}°C | Vibration: {vib} | Status: {status}")

    # Save to file
    with open('elke_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%H:%M:%S"), temp, vib, status])

    time.sleep(1)  # Wait 1 second between readings
