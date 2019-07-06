rm -rf webterminal.tar
docker build  --rm -t pantanal-webssh:1.0.0 ./
docker save -o webterminal.tar pantanal-webssh:1.0.0
