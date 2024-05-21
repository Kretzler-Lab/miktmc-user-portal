# MiKTMC User Portal
Centralized User Portal API for MiKTMC Applications

## Running

edit config.json
```json
{
    "MONGO_URI": "mongodb://portal-mongodb:27018/user-portal?authSource=admin",
    "SECRET_KEY": "create_entropy_to_use_here",
    "ENV": "production",
}
```

`docker compose up -d`
