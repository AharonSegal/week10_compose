
echo "Stopping all running containers..."
docker stop $(docker ps -q) 2>/dev/null || true

echo "Removing all containers..."
docker rm $(docker ps -a -q) 2>/dev/null || true

echo "Removing all images..."
docker rmi -f $(docker images -q) 2>/dev/null || true

echo "Removing all volumes..."
# Remove volumes only if they exist
volumes=$(docker volume ls -q)
if [ ! -z "$volumes" ]; then
  docker volume rm $volumes 2>/dev/null || true
fi

echo "Removing all custom networks..."
# Keep default networks (bridge, host, none)
networks=$(docker network ls -q | grep -v -E "bridge|host|none")
if [ ! -z "$networks" ]; then
  docker network rm $networks 2>/dev/null || true
fi

echo "Full Docker cleanup complete!"
docker system prune -af --volumes
