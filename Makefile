MAKEFLAGS += -s

clean_pycache:
	find . | grep -E "(__pycache__)" | xargs rm -rf

dev:
	flask --app 'backend:create_app("development")' run --host=0.0.0.0 && clean_pycache

test:
	flask --app 'backend:create_app("test")' run --host=0.0.0.0

