FROM armhf/python:3.5
MAINTAINER Fabien Dubosson <fabien.dubosson@qadmium.com>

# Update the distribution and install dependencies from the official repos
RUN apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            nginx \
            supervisor \
            libjpeg-dev \
            python-dev \
            zlib1g-dev \
            python-pil \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

# Install dependencies from pip
RUN pip install uwsgi

# Configure nginx
COPY nginx.conf /etc/nginx/sites-enabled/default
RUN mkdir -p /srv/http/static

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Configure supervisor
COPY supervisord.conf /etc/supervisor/conf.d/

# Configure for raposfly
RUN gpasswd -a www-data dialout
RUN ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/
RUN ln -s /usr/lib/arm-linux-gnueabihf/libfreetype.so /usr/lib/
RUN ln -s /usr/lib/arm-linux-gnueabihf/libz.so /usr/lib/

# Configure uwsgi
RUN mkdir /etc/uwsgi/
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

# Install the application
COPY ./ /app
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN chown www-data:www-data -R /app
RUN python manage.py collectstatic --noinput

WORKDIR /app

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
