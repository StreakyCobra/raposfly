FROM armhf/python:3.5
MAINTAINER Fabien Dubosson <fabien.dubosson@qadmium.com>

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update \
  && apt-get install -t jessie-backports --no-install-recommends --no-install-suggests -y \
            nginx \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            sudo \
            supervisor \
            libjpeg-dev \
            python-dev \
            zlib1g-dev \
            python-pil \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/locale/* /usr/share/man/* /usr/share/doc/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN pip install --upgrade pip && pip install uwsgi

RUN mkdir -p /srv/http/static
RUN mkdir -p /srv/http/media
RUN mkdir -p /etc/uwsgi/
RUN chown -R www-data:www-data /srv/http/

RUN gpasswd -a www-data dialout
RUN ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/
RUN ln -s /usr/lib/arm-linux-gnueabihf/libfreetype.so /usr/lib/
RUN ln -s /usr/lib/arm-linux-gnueabihf/libz.so /usr/lib/

RUN mkdir /var/lib/raposfly/
RUN chown -R www-data:www-data /var/lib/raposfly/

COPY ./ /usr/lib/raposfly/
COPY sudoers.conf /etc/sudoers.d/raposfly
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY supervisord.conf /etc/supervisor/conf.d/
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

WORKDIR /usr/lib/raposfly/
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN chown www-data:www-data -R /usr/lib/raposfly/

VOLUME /var/lib/raposfly/
EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
