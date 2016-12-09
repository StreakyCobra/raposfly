FROM armhf/debian:jessie
MAINTAINER Fabien Dubosson <fabien.dubosson@gmail.com>

RUN apt-get update \
    && apt-get install -y \
      cron \
    && rm -rf /var/lib/apt/lists/*

COPY crontab /etc/cron.d/raposfly
RUN chmod 0644 /etc/cron.d/raposfly
RUN touch /var/log/cron.log

COPY backup.sh /usr/lib/raposfly/backup.sh
RUN chmod +x /usr/lib/raposfly/backup.sh
RUN mkdir -p /var/lib/raposfly/backups/

VOLUME /var/lib/raposfly/

CMD /usr/sbin/cron -L 15 && tail -f /var/log/cron.log
