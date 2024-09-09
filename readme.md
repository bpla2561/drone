python -m venv myenv
. ./myenv/bin/activate
git init
true >__init__.py
deactivate

pip install -r requirements.txt
