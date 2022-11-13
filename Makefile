MAKEFLAGS += -s

dev:
	flask --app 'backend:create_app("development")' run --host=0.0.0.0

test:
	flask --app 'backend:create_app("test")' run --host=0.0.0.0

