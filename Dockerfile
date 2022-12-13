FROM python:3.8-slim

RUN useradd -m informant

COPY --chown=informant:informant ./informant.py /home/informant/informant.py
COPY --chown=informant:informant ./resources.json /home/informant/resources.json
COPY --chown=informant:informant ./requirements /home/informant/requirements

ENV PYTHONPATH /home/informant

WORKDIR /home/informant

RUN /usr/local/bin/python -m pip install --upgrade pip \
    && pip install -r requirements \
    && chmod 755 /home/informant/informant.py

USER informant

CMD ["/home/informant/informant.py"]
