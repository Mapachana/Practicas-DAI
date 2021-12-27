# Dockerfile
FROM python:3.9-alpine

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt &&  apk add --no-cache --upgrade bash libgcc libstdc++ && chmod +x ./dotnet-install.sh && ./dotnet-install.sh -c Current
ENV PATH=$PATH:/root/.dotnet
#RUN  dotnet --list-sdks && dotnet --list-runtimes

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development        
        
CMD ["flask", "run"]
