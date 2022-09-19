FROM python:3.8-slim-buster
RUN ["mkdir","/my_directory"]
COPY generate_and_evaluate.py  /my_directory
WORKDIR /my_directory
CMD ["python3", "generate_and_evaluate.py"]
