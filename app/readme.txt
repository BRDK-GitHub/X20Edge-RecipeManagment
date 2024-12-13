Build and push command:
    docker buildx build --platform linux/arm64,linux/amd64 -t piekutt/webserver --push .

Run command:
    docker run -p 8070:80 piekutt/webserver 