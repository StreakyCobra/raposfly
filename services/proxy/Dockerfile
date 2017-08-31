FROM armhf/debian:jessie

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y -t jessie-backports --no-install-recommends --no-install-suggests \
    nginx \
  && apt-get install -y --no-install-recommends --no-install-suggests \
    ca-certificates \
    gettext-base \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

COPY proxy.conf /etc/nginx/sites-enabled/default

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
