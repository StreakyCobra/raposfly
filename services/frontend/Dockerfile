FROM armhf/debian:jessie

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends --no-install-suggests \
    curl \
    ca-certificates \
  && curl -sL https://deb.nodesource.com/setup_7.x | bash - \
  && apt-get install -y -t jessie-backports --no-install-recommends --no-install-suggests \
    nginx \
  && apt-get install -y --no-install-recommends --no-install-suggests \
    nodejs \
    gettext-base \
    git \
  && apt-get clean \
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
