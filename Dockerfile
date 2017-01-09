###################################
# Jinja2 live parser Dockerfile
#
# Version: 0.1
# Author:  Sonu K. Meena(sahilsk)<sonukr666@gmail.com >
###################################

# Pull base image.
FROM python:2.7

RUN git clone https://github.com/qn7o/jinja2-live-parser.git /data

WORKDIR /data

# Install dependencies
RUN pip install -r requirements.txt

# Change bind host
RUN sed -i 's/host=config.HOST/host="0.0.0.0"/g' parser.py

# Expose port to Host
EXPOSE 5000

# Define default command.
CMD ["python", "parser.py"]
