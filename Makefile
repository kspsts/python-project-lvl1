install: # Установка пакета poetry Install (poetry создаст виртуальное окружение и установит пакет в него)
	poetry install

brain-games: # Запуск скрипта poetry run brain-games
	poetry run brain-games

build: # Команда buildсоздает архивы исходников и колес
	poetry build

publish: # Для отладки публикации мы будем использовать аргумент --dry-run, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run

package-install: # Установка проекта из директории 
	python3 -m pip install --user dist/*.whl