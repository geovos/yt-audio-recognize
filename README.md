# Assessment project

## What this tool does


- Downloads a YT Video based on a user provided URL
- Keeps metrics provided by YT-API
- Extracts the audio out of the video
- Shazams the extracted audio to receive Metadata
- Returns YT-API Metrics + Shazam Metadata as a response to the user
- Stores the related Metadata in PSQL
- Stores the related Metadata in .csv

# Requirements 
 Before you begin, add your key in `YT_API` variable inside `docker-compose.yml`

## Start this project

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```


Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

After you've successfully set up your Docker container you can hit the get endpoint through your browser / postman or any other related tool.

Example endpoint:
`http://localhost:8004/whatsong?video_url=https://www.youtube.com/watch?v=rhTl_OyehF8`

Use to run PSQL inside Docker client.
```sh
$ docker-compose exec db psql -U postgres -d foo
```

## Trouble Shooting


If you encounter errors related to existing migrations remove the migrations directory and start fresh.
Use the below commands.

```sh
docker-compose exec web rm -r migrations
docker-compose exec web alembic init migrations
docker-compose exec web alembic revision --autogenerate -m "Initial migration"
docker-compose exec web alembic upgrade head
```