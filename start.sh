set -e
cd backend && flask run --port=8000 &
cd pifuhd && flask run --port=9696 &
cd pose-estimation && flask run --port=6969 &
cd pix2surf && flask run --port=9191 &
## to kill this, pkill -9 flask 