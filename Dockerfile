FROM python:alpine
WORKDIR /app
COPY main_score.py  .
COPY utils.py  .
RUN pip install Flask
CMD python main_score.py
