# ==================================================================
# Builder image with python 3.10
# ------------------------------------------------------------------
FROM python:3.10-slim AS builder

# ==================================================================
# Python venv
# ------------------------------------------------------------------
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN python3 -m pip install --upgrade pip

# ==================================================================
# Install python packages
# ------------------------------------------------------------------
RUN pip install torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# ==================================================================
# App image with python 3.10
# ==================================================================
FROM python:3.10-slim AS app-images

ENV DEBIAN_FRONTEND=noninteractive
ENV APT_INSTALL="apt-get install -y --no-install-recommends"

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
        ffmpeg
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=builder /venv /venv

# ==================================================================
# App builder
# ------------------------------------------------------------------
ADD app.py /opt/app.py
ADD path.sh /opt/path.sh
ADD apps /opt/apps
ADD services /opt/services
ADD scripts /opt/scripts
ADD config /opt/config
RUN sed -i 's:9008:59008:g' /opt/scripts/run.sh
RUN sed -i 's:${PYENVPATH}/lit:/venv:g' /opt/path.sh

# ==================================================================
# Set Environments
# ------------------------------------------------------------------
WORKDIR /opt
ENV LC_ALL=C.UTF-8
EXPOSE 59008
