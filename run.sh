echo "---------------Starting the dockerized application---------------"
cd frontend 
docker-compose build
docker-compose up -d
docker ps
echo "---------------Successfully deployed over http://0.0.0.0:3000/ ---------------"