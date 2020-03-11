FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

RUN apk add gcc musl-dev libffi-dev openssl-dev make

ARG _APP_DIR="/app"
ARG _USER="app"

# add user
RUN addgroup -S $_USER && adduser -u 1001 -S ${_USER} -G $_USER

# Install python dependecies
WORKDIR ${_APP_DIR}/
COPY --chown=${_USER}:${_USER} ./requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY --chown=${_USER}:${_USER} ./ .


RUN chown -R ${_USER} ${_APP_DIR}
USER ${_USER}
WORKDIR ${_APP_DIR}/

CMD ["python", "main.py"]
