#!/bin/bash
docker-compose build
docker-compose up -d
sleep 5  # Espera o banco iniciar
docker-compose exec web alembic revision --autogenerate -m "init"
docker-compose exec web alembic upgrade head
echo "✅ API PRONTA em http://localhost:8000"
docker-compose logs web -f
