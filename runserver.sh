#!/bin/sh

while true;
do
    rc=`nc -z ${DB_HOST} 5432 &> /dev/null; echo $?`

    if [[ ${rc} -eq 0 ]];
    then
        echo "PostgresDB available!"
        break
    fi

    echo "Waiting PostgresDB... Status is ${rc}"
    sleep 2
done

./manage.py migrate
./manage.py collectstatic --noinput

./manage.py runserver 0.0.0.0:${PORT}
