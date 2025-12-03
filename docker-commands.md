# Docker Commands Reference

## Build
```bash
docker build -t hunter-api .
```

## Run
```bash
docker run -p 8000:8000 hunter-api
```

## Run with volume (persist data)
```bash
docker run -p 8000:8000 -v $(pwd)/data:/app/data hunter-api
```

## Stop
```bash
docker stop $(docker ps -q --filter ancestor=hunter-api)
```

## Remove
```bash
docker rmi hunter-api
```