start_backend:
	python3 -m flask --app ./main.py run

start_backend_debug:
	python3 -m flask --app ./main.py --debug run

start_frontend:
	cd frontend && npm start

start_venv:
	source ./env/bin/activate

install_requirement:
	pip3 install -r requirements.txt