ARG PORT=443



FROM cypress/browsers:latest


RUN apt-get install python3 -y

RUN echo $(python3 -m site --user-base)

COPY requirements.txt  .

ENV PATH /home/root/.local/bin:${PATH}



RUN  apt-get update && apt-get install -y python3-pip && pip install --upgrade pip && pip install -r requirements.txt && pip install "fastapi[all]"
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# Instalar ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver



COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port $PORT





