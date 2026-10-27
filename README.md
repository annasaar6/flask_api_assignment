# flask_api_assignment

Flask API Assignment
Overview
This project demonstrates:

Flask GET endpoint
Flask POST endpoint
JSON request processing
Error handling
Automated testing with pytest
Setup
Create virtual environment:

python -m venv venv
Activate:

Windows:

venv\Scripts\activate
Mac/Linux:

source venv/bin/activate
Install dependencies:

pip install Flask pytest
Run Server
python app.py
Server starts at:

http://127.0.0.1:5000
Endpoints
GET /hello
Optional query parameter:

/hello?name=Alice
POST /sum
Example request:

{
  "numbers": [1, 2, 3]
}
Example response:

{
  "numbers": [1, 2, 3],
  "sum": 6,
  "status": "success"
}
Run Tests
pytest test_app.py
Expected result:

6 passed

___________________________________________________________________________________________________________________________
PS C:\Users\vboxuser\Desktop\762-assignments\module_2_project_2\flask_api_assignment> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\vboxuser\Desktop\762-assignments\module_2_project_2\flask_api_assignment\venv\Scripts\Activate.ps1)
(venv) PS C:\Users\vboxuser\Desktop\762-assignments\module_2_project_2\flask_api_assignment> & c:\Users\vboxuser\Desktop\762-assignments\module_2_project_2\flask_api_assignment\venv\Scripts\python.exe c:/Users/vboxuser/Desktop/762-assignments/module_2_project_2/flask_api_assignment/venv/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-011-674
127.0.0.1 - - [27/Oct/2026 14:53:09] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [27/Oct/2026 14:58:00] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [27/Oct/2026 14:58:06] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [27/Oct/2026 15:03:47] "GET /hello?name=Alice HTTP/1.1" 200 -
127.0.0.1 - - [27/Oct/2026 15:05:18] "POST /sum HTTP/1.1" 200 -
 * Detected change in 'c:\\Users\\vboxuser\\Desktop\\762-assignments\\module_2_project_2\\flask_api_assignment\\venv\\test_app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-011-674
 * Detected change in 'c:\\Users\\vboxuser\\Desktop\\762-assignments\\module_2_project_2\\flask_api_assignment\\venv\\test_app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-011-674
127.0.0.1 - - [27/Oct/2026 15:24:05] "GET / HTTP/1.1" 404 -
