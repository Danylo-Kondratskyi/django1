set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# Frontend setup
npm install                # Install Node.js dependencies (if you have a package.json)
npm run build              # Build the JavaScript assets