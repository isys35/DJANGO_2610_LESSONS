docker run \
-d \
-e POSTGRES_PASSWORD=isysbas \
-e POSTGRES_USER=isysbas \
-e POSTGRES_DB=classroom \
-p 5433:5432 \
postgres