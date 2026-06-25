.PHONY: help up down build logs clean migrate test

help:
	@echo "SMART QHSE Platform Commands"
	@echo "============================"
	@echo "make up        - Start all services"
	@echo "make down      - Stop all services"
	@echo "make build     - Build Docker images"
	@echo "make logs      - Show logs"
	@echo "make clean     - Remove containers and volumes"

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

clean:
	docker-compose down -v
