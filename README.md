# Docker Hit Counter

A simple Flask web app that counts page visits, using Redis as a
persistent counter store. Built to practice Docker fundamentals:
custom images, multi-container orchestration with docker-compose,
and container-to-container networking via Docker DNS.

## Stack
- Python 3.11 + Flask
- Redis (persistent counter)
- Docker + docker-compose

## Run it

    docker-compose up -d
    curl localhost:5000
