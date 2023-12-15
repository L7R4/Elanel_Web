#!/bin/bash

export FECHA=`date +%d_%m_%Y_%H_%M_%S`
export NAME=elanelweb_${FECHA}.dump
export DIR=/home/elanelweb/backup/
USER_DB=postgres
NAME_DB=elanelweb
cd $DIR
> ${NAME}
export PGPASSWORD=klf781CL
chmod 777 ${NAME}
echo "Realizando backup"
pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
echo "Backup finalizado"
