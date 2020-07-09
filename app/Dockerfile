FROM python:3.8

RUN mkdir /dependencias
RUN mkdir /codigo
RUN mkdir /start

COPY requeriments.txt /dependencias
RUN pip3 install -r /dependencias/requeriments.txt

ENV SECRET_KEY=""
ENV DB_NAME=""
ENV DB_USER=""
ENV DB_PASSWORD=""
ENV DB_HOST=""
ENV DB_PORT=3306


COPY inicia_proyecto.sh /start
RUN useradd -s /bin/bash limitado 
RUN chown -R limitado  /codigo
RUN chown -R limitado  /start

USER limitado
RUN chmod +x /start/inicia_proyecto.sh
WORKDIR /codigo
CMD /start/inicia_proyecto.sh
