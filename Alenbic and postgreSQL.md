Alembic - построен поверх SQLAlchemy
Умеет автоматически генерировать код миграций.

ОСНОВНЫЕ КОММАНДЫ
alembic upgrade head - накатить все
alembic downgrade -1 - откатить одно
alembic revision --autogenerate -m 'комментарий, поясняющий миграцию' - генерация миграции
alembic revision --autogenerate -m "TeamMember extensions"
alembic current - где находится текущий head. хеш текущей миграции

1. Необходимо проверять откат миграций и дорабатывать их в ручную.
op.create_foreign_key('team_members_city_id_fkey', 'team_members', 'cities', ['city_id'], ['id']) - добавлено имя ключа team_members_city_id_fkey
   
op.execute('DROP TYPE team_member_status_type') - такими образом можно выполнить sql код 

УДАЛЕНИЕ БД ПРИВОДИТ К УДАЛЕНИЮ ВСЕХ МИГРАЦИЙ

### PostgreSQL

##### Подключение к базе
sudo su postgres
psql


 - удалить базу
sudo -u postgres dropdb roompark;
sudo -u postgres psql -c "CREATE DATABASE roompark OWNER roompark"

sudo -u postgres psql -c "CREATE USER roompark ENCRYPTED PASSWORD 'roompark'"
sudo -u postgres psql -c "CREATE DATABASE roompark OWNER roompark"

