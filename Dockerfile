FROM python:3.12

WORKDIR /aiogram_bot

COPY requirements.txt /aiogram_bot
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /aiogram_bot

CMD [ "python", "./main.py" ]
