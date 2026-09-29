![CI](https://github.com/a-elef93/docker-hit-counter/actions/workflows/ci.yml/badge.svg)
# Docker Hit Counter

A simple Flask web app that counts page visits, using Redis as a
persistent counter store. Built to practice Docker fundamentals:
custom images, multi-container orchestration with docker-compose,
and container-to-container networking via Docker DNS.

## Stack
- Python 3.11 + Flask
- Redis (persistent counter)
- Docker + docker-compose
  
## CI/CD
This project uses **GitHub Actions** to automatically validate every push to `main`.
The pipeline (`.github/workflows/ci.yml`) runs on a fresh Ubuntu runner and:

1. Checks out the repository code
2. Builds the Docker image and starts the app with Docker Compose (Flask + Redis)
3. Runs a **smoke test**: sends a request to the app and verifies the response contains the expected text
4. Prints the container logs if any step fails, to make debugging easier

### Lessons learned
While building the pipeline I debugged a real failure: the smoke test failed with
`curl: (56) Connection reset by peer` because the request was sent before the Flask
app was ready. I fixed it by adding `--retry-all-errors` so curl retries until the
app is up.

## Run it

    docker-compose up -d
    curl localhost:5000
