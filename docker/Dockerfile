FROM phusion/baseimage:0.9.15
MAINTAINER Albert Lacarta <urodoz@gmail.com>

ENV HOME /root
CMD ["/sbin/my_init"]

#Install Dependencies
RUN apt-get update
RUN apt-get install -y python software-properties-common python-pip
RUN apt-get install -y python-dev build-essential gcc git-core libmysqlclient-dev mysql-client

#Python libraries
RUN pip install Flask Flask-Testing Flask-API
RUN pip install requests MySQL-python lurker nose

RUN mkdir /code
WORKDIR /code

EXPOSE 3000

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*