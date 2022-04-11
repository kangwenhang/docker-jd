FROM python:3.9
ENV VENV_PATH="/venv"
ENV PATH="$VENV_PATH/bin:$PATH"
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get upgrade -y && \
    apt-get install ffmpeg tesseract-ocr -y && \
    apt-get autoclean \
    apt-get git
RUN pip install --upgrade poetry
RUN python -m venv /venv \
&& git clone -b https://github.com/aahnik/tgcf.git /app/dir/
RUN poetry build && \
    /venv/bin/pip install --upgrade pip wheel setuptools &&\
    /venv/bin/pip install dist/*.whl
CMD ["/bin/bash"]