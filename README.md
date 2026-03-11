# rtag-prod
The production stack for rTag, the game.

## Local Development
In order to run a local dev server, use docker-compose from the repo root directory.

```bash
# Start local dev server.
docker-compose up
```

### Running Tests
Attach to the running rTag container.
```bash
docker exec -it <container_id> sh
```
Use Django to run the tests.
```bash
python manage.py test
```

### Linting
Run Flake8 from the repo root directory for a linting report.
```bash
flake8
```
