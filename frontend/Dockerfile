FROM armhf/debian:jessie
MAINTAINER Fabien Dubosson <fabien.dubosson@gmail.com>

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            curl \
            ca-certificates \
  && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get install -t jessie-backports --no-install-recommends --no-install-suggests -y \
            nginx \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            nodejs \
            gettext-base \
            git \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./ /usr/lib/raposfly/
COPY nginx.conf /etc/nginx/sites-enabled/default

WORKDIR /usr/lib/raposfly/
RUN npm install && npm run build

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
