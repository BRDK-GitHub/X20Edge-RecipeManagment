Build and push command:
    docker buildx build --platform linux/arm64,linux/amd64 -t piekutt/opc-ua --push .

Run command:
    docker run -p 5000:5000 piekutt/opc-ua_server