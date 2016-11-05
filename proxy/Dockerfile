FROM armhf/debian:jessie
MAINTAINER Fabien Dubosson <fabien.dubosson@gmail.com>

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update \
  && apt-get install -t jessie-backports --no-install-recommends --no-install-suggests -y \
            nginx \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            ca-certificates \
            gettext-base \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

COPY proxy.conf /etc/nginx/sites-enabled/default

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
