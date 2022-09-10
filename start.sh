set -e
cd backend && flask run --port=8000 &
cd pifuhd && flask run --port=9696 &
cd pose-estimation && flask run --port=6969 &

## to kill this, pkill -9 flask 