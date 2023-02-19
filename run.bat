cd /D "%~dp0"
docker rm -f devenv
docker compose build
docker compose run --name devenv --rm --service-ports devenv
