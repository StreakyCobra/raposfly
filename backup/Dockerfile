FROM armhf/debian:jessie

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends --no-install-suggests \
    cron \
    rsyslog \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

RUN touch /etc/crontab
RUN touch /var/log/cron.log

COPY crontab /tmp/crontab
RUN crontab /tmp/crontab && rm /tmp/crontab

COPY backup.sh /usr/lib/raposfly/backup.sh
RUN chmod +x /usr/lib/raposfly/backup.sh

VOLUME /var/lib/raposfly/

CMD rsyslogd && cron && tail -f /var/log/cron.log /var/log/syslog
