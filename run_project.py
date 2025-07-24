import subprocess
import webbrowser
import os
import time

# Start the Flask backend
print("Starting backend server...")

backend_path = os.path.join(os.getcwd(), 'backend', 'app.py')

try:
    subprocess.Popen(["python", backend_path], shell=True)
except Exception as e:
    print("Error starting backend:", e)

# Wait a moment to ensure the server starts
time.sleep(2)

# Open the frontend in the browser
frontend_path = os.path.join(os.getcwd(), 'frontend', 'Template', 'index.html')

if os.path.exists(frontend_path):
    webbrowser.open('file://' + frontend_path)
else:
    print("Frontend file not found:", frontend_path)
