FROM armhf/debian:jessie
MAINTAINER Fabien Dubosson <fabien.dubosson@gmail.com>

# Install nginx
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

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

# Install node
RUN apt-get update && apt-get install -y curl git
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/locale/* && rm -rf /usr/share/man/* && rm -rf /usr/share/doc/*

# Copy the proxy configuration
COPY nginx.conf /etc/nginx/sites-enabled/default

# Build the frontend
COPY ./ /app
WORKDIR /app
RUN npm install && npm run build

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
