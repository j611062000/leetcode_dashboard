start:
	python3 -m flask --app ./main.py run

start_debug:
	python3 -m flask --app ./main.py --debug run

start_venv:
	source ./env/bin/activate

install_requirement:
	pip3 install -r requirements.txt