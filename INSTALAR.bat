ECHO ON

python -m venv venv
venv\Scripts\python.exe -m pip install --require-virtualenv -r requirements.txt
venv\Scripts\python.exe -m pip freeze

cmd /k