PYTHON = python3
SERVER_FILE = server.py 

all: install_dependencies start_fastapi

start_fastapi: 
	@cd core/ && fastapi dev server.py

clean:
	@rm -rf core/__pycache__

install_dependencies: 
	@pip install -r requirements.txt