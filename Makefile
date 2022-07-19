#-*-makefile-*-

TOPLVL  = .

include $(TOPLVL)/Makefile.config

install:
	@echo "Installing python dependencies."
	@pip3 install --user -r requirements.txt

start:
	@echo "Starting NAF Python connector at port: $(URL_PY_PORT)"
	@nohup sh -c "gunicorn --bind 0.0.0.0:$(URL_PY_PORT) --workers $(URL_GUNICORN_WORKERS) --threads $(URL_GUNICORN_THREADS) --timeout 1200 app_ui:app_ui>>/tmp/url_python_gunicorn.log 2>&1" &

status:
	@ps -ef | grep "gunicorn --bind 0.0.0.0:$(URL_PY_PORT)"

stop:
	@echo "Stopping NAF python connector."
	@pkill -f "gunicorn --bind 0.0.0.0:$(URL_PY_PORT)"

clean:
	@echo "Removing all generated python executables."
	@find . | grep -E "__pycache__" | xargs rm -rf
	@find . | grep -E ".pyc" | xargs rm -rf
	@find . | grep -E ".pyo" | xargs rm -rf

