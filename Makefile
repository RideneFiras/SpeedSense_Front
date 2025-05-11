# Local FastAPI dev server
fastapi:
	uvicorn app:app --reload

# Build Docker image locally
build:
	docker build -t speedsense-app .

# Run Docker container locally
run:
	docker run -d -p 8080:8080 speedsense-app 

# Stop running container(s) from this image
stop:
	docker stop $(docker ps -q --filter ancestor=speedsense-app)

# Tag and push to Docker Hub with a given tag (e.g., make push TAG=latest)
push:
ifndef TAG
	$(error ❌ TAG is not set. Usage: make push TAG=latest)
endif
	docker tag speedsense-app firasrid/speedsense-app:$(TAG)
	docker push firasrid/speedsense-app:$(TAG)
