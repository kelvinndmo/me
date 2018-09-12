import os
from app import create_app


app = create_app(os.getenv("CONFIG_STAGE") or "default")

if __name__ == '__main__':
    app.run(debug=True)
source venv/bin/activate


export FLASK_APP="run.py"
export MODE = "development"
export FLASK_DEBUG=1
