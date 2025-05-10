fastapi:
	uvicorn app:app --reload

build:
	docker build -t speedsense-app .

run:
	docker run -d -p 8000:8000 speedsense-app
stop:
	docker stop $(docker ps -q --filter ancestor=speedsense-app)
	
	