migration:
	docker-compose exec web alembic revision --autogenerate -m "$(M)"

migrate:
	docker-compose exec web alembic upgrade head

revert_last_migration:
	docker-compose exec web alembic downgrade -1

revert_migration_id:
	docker-compose exec web alembic downgrade $(V)

history:
	docker-compose exec web alembic history

current:
	docker-compose exec web alembic current