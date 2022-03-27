set -e
cd backend && flask run --port=8000 &
cd pifuhd && flask run --port=9696 &
cd lightweight-human-pose-estimation.pytorch && flask run --port=6969 &