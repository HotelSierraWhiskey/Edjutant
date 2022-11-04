dev:
	flask --app 'backend:create_app("dev")' run --host=0.0.0.0

prod:
	flask --app 'backend:create_app("prod")' run