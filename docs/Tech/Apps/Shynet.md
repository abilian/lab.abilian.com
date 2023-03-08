Shynet is a modern, privacy-friendly, and detailed web analytics that works without cookies or JS.

Techno used: Django on the backend. Nothing fancy on the front-end.

Nicely done installation guide: https://github.com/milesmcc/shynet/blob/master/GUIDE.md

## Pros and cons
### Pros
- Simple to install and operate.

### Cons
- Not very accurate in terms of filtering false sessions.

## Sysadmin notes
### To install
```
cd /home/docker-apps
git clone https://github.com/milesmcc/shynet/
# edit .env
docker-compose up -d
```

### To upgrade
```
cd /home/docker-apps/shynet
git pull
docker-compose stop
docker rm shynet_main
docker pull milesmcc/shynet:latest
docker-compose up -d
```
