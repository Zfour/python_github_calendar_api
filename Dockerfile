FROM python:3-alpine

LABEL name="python_github_calendar_api" \
    repository="https://github.com/Zfour/python_github_calendar_api" \
    contrubutors="Zfour, ShengQiBaoZao, seeleclover"

ENV TZ=Asia/Shanghai

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "__init__.py" ]
