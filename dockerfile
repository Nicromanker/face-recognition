FROM python:3.9

RUN apt-get update && apt-get install cmake ffmpeg libsm6 libxext6  -y

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
