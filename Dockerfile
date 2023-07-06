###################################
# Jinja2 live parser Dockerfile
#
# Version: 0.1
# Author:  Sonu K. Meena(sahilsk)<sonukr666@gmail.com >
###################################

# Pull base image.
FROM python:2.7-alpine

# Copy files
COPY . /data
WORKDIR /data

# Install dependencies
RUN pip install -r requirements.txt

# Make host accessible. See config.py for more options
ENV HOST 0.0.0.0

# Expose port to Host
EXPOSE 5000

# Define default command.
CMD ["python", "parser.py"]
