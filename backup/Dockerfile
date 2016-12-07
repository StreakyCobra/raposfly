FROM debian:jessie-backports
MAINTAINER Fabien Dubosson <fabien.dubosson@gmail.com>

RUN apt-get update \
    && apt-get install -y \
      cron \
    && rm -rf /var/lib/apt/lists/*

RUN echo '*/5 * * * * /opt/backup.sh' >> /tmp/crontab \
    && crontab /tmp/crontab \
    && rm /tmp/crontab

COPY backup.sh /opt/backup.sh

VOLUME /app

CMD ["/usr/bin/cron", "-f"]
