# miktmc_user_portal
Centralized User Portal API for MiKTMC Applications


## Development Environment
#### Config
```sh
git clone https://github.com/Kretzler-Lab/miktmc-user-portal/
cd miktmc-user-portal
touch config.json
touch .docker.env
```

config.json
```json
{
    "MONGO_URI": "mongodb://mongodb:27017/user-portal?authSource=admin",
    "SECRET_KEY": "create_entropy_to_use_here",
    "ENV": "development",
}
```

#### Mongo Variables
.docker.env
```env
MONGO_ROOT_USERNAME=root
MONGO_ROOT_PASSWORD={MONGO_ROOT_PASSWORD}
```
then

`docker-compose up`
