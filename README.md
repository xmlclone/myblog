# Myblog
flask as backend, frontend use jquery and bootstrap etc.

# Usage
1. Use `pip install -r requirements.txt` to install library.
2. Create `instance` direcory in your porject.
3. Move `config.py` to `instance` and change something you need.
4. Use `flask --app blog init-db` to initialize models.

> pip mirro: https://pypi.tuna.tsinghua.edu.cn/simple

# Deploy

Use `Gunicorn`.

## Installing

```shell
pip install gunicorn
```

## Running

```shell
# equivalent to 'from hello import app'
gunicorn -w 4 'hello:app'

# or
# equivalent to 'from hello import create_app; create_app()'
gunicorn -w 4 'hello:create_app()'

# bind，0.0.0.0 is not a valid address to navigate to, you’d use a specific IP address in your browser
gunicorn -b 0.0.0.0

# bind port, default is 8000
gunicorn -b 127.0.0.1:8083
```