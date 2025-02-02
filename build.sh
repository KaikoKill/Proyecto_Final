set - o errexit

# Build the project

# Install dependencies
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate