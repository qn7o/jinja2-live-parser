FROM python:2.7

RUN git clone https://github.com/guymatz/jinja2-live-parser.git
WORKDIR jinja2-live-parser
RUN ./setup.sh

EXPOSE 5000

#ENTRYPOINT ./run.sh
CMD ./run.sh
