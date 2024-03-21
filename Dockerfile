FROM python:3.10

ENV HOME=/app
RUN mkdir $HOME
RUN mkdir $HOME/staticfiles
RUN mkdir $HOME/media
# set work directory
WORKDIR $HOME


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install netcat-traditional
RUN apt-get update && apt-get install -y netcat-traditional



# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]