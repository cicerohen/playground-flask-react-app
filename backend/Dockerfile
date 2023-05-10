FROM python:3.10-alpine3.15

RUN pip install --upgrade pip
RUN pip install pipenv

ARG USER

RUN adduser -D ${USER}
USER ${USER}

RUN mkdir /home/${USER}/app

WORKDIR /home/${USER}/app

ENV PATH="/home/${USER}/.local/bin:${PATH}"

COPY --chown=${USER}:${USER} Pipfile Pipfile
RUN  pipenv install --deploy --ignore-pipfile

COPY --chown=${USER}:{USER} . .

CMD ["pipenv", "run", "python", "app.py"]

