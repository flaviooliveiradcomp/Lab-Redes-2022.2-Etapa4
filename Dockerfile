FROM python:3-slim
LABEL version="1.0.0" description="Etapa4" maintainer="Flavio Emanuel <flavio.oliveira@dcomp.ufs.br>"
WORKDIR /usr/src/flavio-etapa4
COPY . .
EXPOSE 12000
CMD [ "python", "./TCPServer.py" ]
