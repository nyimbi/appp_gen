
# Introspect this database t2x and write the t2xx
# Now we create the second version of the database after manually editing the models.py
# now we create database
chmod +x second.sh fourth.sh
dropdb t2xx
createdb t2xx
python3 gen.py -w /Volumes/Media/src/pjs/auplat/plat/app -i t2x -c t2xx 
    