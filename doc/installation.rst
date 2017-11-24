============
Installation
============

First you can go through the list of requirements to be sure that you have
everything. Then you can follow the section explaining how to prepare your
Raspberry Pi, and finally follow the section about deploying the project on the
device.

-----

.. contents:: **Table of Contents**

-----

Requirements
------------

These are the minimum requirements to run *raposfly*:

-  Raspberry Pi 3
-  Power plug
-  Ethernet cable
-  MicroSD card ``>= 8G``
-  MicroSD to SD apdapter
-  SD card reader
-  Thermal printer supported by the python-escpos_ library.

.. _python-escpos: https://github.com/python-escpos/python-escpos

Preparation of the Raspberry Pi
-------------------------------

In order to run *raposfly*, the Raspberry Pi should be prepared for serving as a
WIFI access point, with a DHCP server, a DNS server, a firewall, a docker engine
and an USB setup to access the printer. It is quite a lot, but these steps only
have to be done once.

This procedure has been tested on the version:

.. figure:: https://img.shields.io/badge/raspbian--lite-Mars%202017-brightgreen.svg
   :alt: Mars 2017

.. figure:: https://img.shields.io/badge/raspbian--lite-September%202017-orange.svg
   :alt: September 2017

(WIP for September 2017)

Install and configure the rasbian-lite distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get raspbian-lite_:

-  `Direct download`_
-  `Torrent download`_

Usually downloading by torrent is faster than direct download.

`Write the image file`_ to the microSD card by using the microSD to SD adapter
and the SD card reader.

Before going further, the ``SSH`` service need to be activated. For this mount
the ``boot`` partition of the SD card to your system and create an empty ``ssh``
file in it, as explained in the point 3 of `enable ssh`_.

Once this has been done, you can put the SD card in the Rasberry Pi, plug the
ethernet cable and power it up. The rest of the procedure is meant to be run on
the Rasberry Pi directly. For this you will need to `find the IP address`_ of
the Rasberry on the network, and `ssh into it`_ (default password for the ``pi``
account is ``raspberry``):

.. References

.. _raspbian-lite: https://www.raspberrypi.org/downloads/raspbian/
.. _`Direct download`: https://downloads.raspberrypi.org/raspbian_lite_latest
.. _`Torrent download`: https://downloads.raspberrypi.org/raspbian_lite_latest.torrent
.. _`Write the image file`: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
.. _`enable ssh`: https://www.raspberrypi.org/documentation/remote-access/ssh/
.. _`find the ip address`: https://www.raspberrypi.org/documentation/remote-access/ip-address.md
.. _`ssh into it`: https://www.raspberrypi.org/documentation/remote-access/ssh/

.. code-block:: console

    ssh pi@192.168.1.100

First the distribution can be updated with:

.. code-block:: console

    sudo apt update
    sudo apt upgrade -y

You may want to install ``vim`` if you prefer this over ``nano``:

.. code-block:: console

    sudo apt install -y vim

Whenever you need to edit or create a file, depending on your preferences you
will need to either use:

.. code-block:: console

    sudo nano /path/to/filename

or

.. code-block:: console

    sudo vim /path/to/filename

Before going further, be sure to restart your Raspberry Pi in order to reload
the kernel as it has probably be updated:

.. code-block:: console

    sudo reboot

Wait one minute then reconnect to your Rasberry Pi with SSH after for continuing
the installation procedure.

Install and configure the WIFI access-point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use the Raspberry Pi as an access point, ``hostapd`` need to be
installed, as well as ``iptables-persistent`` that is needed to restore the
defined routes at each boot:

.. code-block:: console

    sudo apt install -y hostapd iptables-persistent

Answer ``No`` to the 2 questions that are asked about ``iptables-persistent``.

Create the file ``/etc/hostapd/hostapd.conf`` and add the following content:

.. code-block:: cfg

    interface=wlan0
    ssid=Pi_AP
    country_code=US
    hw_mode=g
    channel=6
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_passphrase=Raspberry
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=CCMP
    wpa_group_rekey=86400
    ieee80211n=1
    wme_enabled=1

Be sure to personalize this to set a custom ``ssid`` and a custom
``wpa_passphrase``. This will allow you to identify more easily your Raspberry
Pi network, and prevent other people to connect to your network with the default
credential.

Then you need to edit the file ``/etc/default/hostapd`` to indicate where to
find the configuration file we just created:

.. code-block:: cfg

    DAEMON_CONF="/etc/hostapd/hostapd.conf"

*Note:* Be sure to remove the ``#`` in front of the line

Edit the file ``/etc/init.d/hostapd`` in the same vein to indicate which
configuration file to use:

.. code-block:: cfg

    DAEMON_CONF=/etc/hostapd/hostapd.conf

Edit the ``/etc/sysctl.conf`` file and uncomment the line to enable ip
forwarding:

.. code-block:: cfg

    net.ipv4.ip_forward=1

Run this command to activate it for the current session without rebooting:

.. code-block:: console

    sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

Create the NAT rules to redirect ``wlan0`` trafic to ``eth0``:

.. code-block:: console

    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
    sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

And save them to be restored at boot time by ``iptables-persistent``:

.. code-block:: console

    sudo sh -c "iptables-save > /etc/iptables/rules.v4"

Remove the WPA supplicant service as it's not needed anymore:

.. code-block:: console

    sudo mv /usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service /root/

And finally make ``hostapd`` to start at boot:

.. code-block:: console

    sudo systemctl enable hostapd

Install and configure the DHCP server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to get an IP address when connecting to the Wifi, a DHCP server is
needed. The ``isc-dhcp-server`` package should be installed for this:

.. code-block:: console

    sudo apt install -y isc-dhcp-server

Then edit ``/etc/dhcp/dhcpd.conf`` to comment out the following lines:

.. code-block:: cfg

    # option definitions common to all supported networks...
    #option domain-name "example.org";
    #option domain-name-servers ns1.example.org, ns2.example.org;

And in the same file uncomment the ``authoritative`` line:

.. code-block:: cfg

    # If this DHCP server is the official DHCP server for the local
    # network, the authoritative directive should be uncommented.
    authoritative;
     
And finally, at the end of the same file, add the following lines:

.. code-block:: cfg

    subnet 192.168.42.0 netmask 255.255.255.0 {
        range 192.168.42.10 192.168.42.100;
        option broadcast-address 192.168.42.255;
        option routers 192.168.42.1;
        default-lease-time 600;
        max-lease-time 7200;
        option domain-name "raposfly.shop";
        option domain-name-servers 192.168.42.1;
    }

Then edit ``/etc/default/isc-dhcp-server`` and set ``INTERFACESv4`` to ``wlan0``
so that the DCHP server is listening on the Wifi:

.. code-block:: cfg

    INTERFACESv4="wlan0"

The Raspberry Pi should have a fixed address, so not getting it through DHCP.
For this edit the file ``/etc/dhcpcd.conf`` and add the following lines:

.. code-block:: cfg

    interface wlan0
    static ip_address=192.168.42.1

Set manually the ip address for this session:

.. code-block:: console

    sudo ifconfig wlan0 192.168.42.1

It appears that isc-dhcp-server may start before dhcpcd gives an address to
``wlan0``, what causes a bug. In order to avoid this, add ``sleep 10`` at the
beginnig of the ``start_daemon`` function in ``/etc/init.d/isc-dhcp-server``:

.. code-block:: cfg

    start_daemon()
    {
        VERSION="$1"
        CONF="$2"
        NAME="$3"
        PIDFILE="$4"
        DESC="$5"

        shift 5
        INTERFACES="$*"

        sleep 10

        test_config "$VERSION" "$CONF"
        log_daemon_msg "Starting $DESC" "$NAME"

And finally make ``isc-dhcp-server`` to start at boot:

.. code-block:: console

    sudo systemctl enable isc-dhcp-server

Install and configure the DNS server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have a DHCP server, we need a name server that will allow us to
access ``raposfly`` from the clients directly with a name, not with a IP
address. For this the ``dnsmasq`` package should be installed:

.. code-block:: console

    sudo apt install -y dnsmasq

Edit ``/etc/dnsmasq.conf`` to uncomment and change the following lines:

.. code-block:: cfg

    domain-needed
    bogus-priv
    local=/raposfly.shop/
    domain=raposfly.shop
    interface=wlan0

Add also this at the end of the file so that all URLs will redirect to the
Rapsberry Pi:

.. code-block:: cfg

    address=/raposfly.shop/192.168.42.1

Finally enable the DNS server at boot:

.. code-block:: console

    sudo systemctl enable dnsmasq

Install and configure the UFW firewall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to install a firewall, the ``ufw`` package should be install with:

.. code-block:: console

    sudo apt install -y ufw

Prevent it to block your current SSH connection before starting it:

.. code-block:: console

    sudo ufw allow 22

Open also port that will be used later: 80 for HTTP, and 53 for DNS

.. code-block:: console

    sudo ufw allow 80
    sudo ufw allow 53

We also want containers in the docker network to communicate together:

.. code-block:: console

    sudo ufw allow from 172.16.0.0/12

Start it right away:

.. code-block:: console

    sudo ufw enable

Verify that the rules have been added, better to be sure for SSH (22):

.. code-block:: console

    sudo ufw status verbose

Set UFW to start on boot:

.. code-block:: console

    sudo systemctl enable ufw

Install and configure the Docker engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to run the code, a docker engine is needed. You can obtain and install
docker with:

.. code-block:: console

    curl -sSL https://get.docker.com/ | sh

Your user need to be in the docker group to be able to use docker:

.. code-block:: console

    sudo gpasswd -a $USER docker

In order to manage the docker containers with simplicity, ``docker-compose``
should be installed:

.. code-block:: console

    sudo apt update
    sudo apt install -y apt-transport-https dirmngr
    echo "deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ jessie main" | sudo tee /etc/apt/sources.list.d/hypriot.list
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 37BBEE3F7AD95B3F
    sudo apt update
    sudo apt install -y docker-compose

Docker has the bad habit to play with iptables, what have a tendency to break
UFW rules, so we need the following steps to prevent this:

Edit ``/etc/default/ufw`` in order to allow UFW to forward request to docker:

.. code-block:: cfg

    DEFAULT_FORWARD_POLICY="ACCEPT"

Modify the file ``/etc/systemd/system/multi-user.target.wants/docker.service``
in order to prevent docker to play with iptables:

.. code-block:: cfg

    ExecStart=/usr/bin/dockerd -H fd:// --iptables=false

Add the following block on the top of ``/etc/ufw/before.rules`` in order to
allow docker to access the outside world:

.. code-block:: cfg

    #
    # rules.before
    #
    # Rules that should be run before the ufw command line added rules. Custom
    # rules should be added to one of these chains:
    #   ufw-before-input
    #   ufw-before-output
    #   ufw-before-forward
    #

    # nat Table rules
    *nat
    :POSTROUTING ACCEPT [0:0]

    # Forward trafic from docker through eth0.
    -A POSTROUTING -s 172.16.0.0/12 -o eth0 -j MASQUERADE

    # Don't delete the 'COMMIT' line or these nat table rules won't be processed
    COMMIT

Finally we can set docker to start at boot:

.. code-block:: console

    sudo systemctl enable docker

Install and configure the USB driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to allow access to USB devices to users of the ``dialout`` group, we
need to create a new file ``/etc/udev/rules.d/99-usb-dialout.rules``:

.. code-block:: cfg

    SUBSYSTEM=="usb", DRIVER=="usb", MODE="0664", GROUP="dialout"

You should now add yourself to the ``dialout`` group that has access now to the
USB device:

.. code-block:: console

    sudo gpasswd -a $USER dialout

Verification
~~~~~~~~~~~~

Now that everything has been done, it's time to reboot to see if everything is
working as excepted:

.. code-block:: console

    sudo reboot

You should now be able to:

- Connect to the Wifi provided by the Raspberry Pi with your laptop/phone
- Access internet through the Wifi of the connected client
- SSH into the Raspberry Pi through the Wifi (192.168.42.1)
- Check that the firewall is running with ``sudo ufw status``
- See docker information with ``docker info``

If yes, you are on the good way!

Deployement of the project
--------------------------

Now that the base of the Raspberry Pi is configured, we can put the code on it
and start the deploying the application.

For this we will first need to install ``git``:

.. code-block:: console

    sudo apt install -y git

Clone the project on the Raspberry PI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the project on the rapsberry with the following command:

.. code-block:: console

    git clone https://github.com/StreakyCobra/raposfly.git

If you have your own version of the code, for instance if you have made some
modifications in a fork, you can simply change the URL to your one.

Prepare database and file structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sqlite database file and the backup folder should be created with:

.. code-block:: console

    sudo mkdir -p /var/lib/raposfly/backups/
    sudo touch /var/lib/raposfly/db.sqlite3
    sudo chown -R www-data:www-data /var/lib/raposfly/

Build the containers
~~~~~~~~~~~~~~~~~~~~

The containers can simply be built with:

.. code-block:: console

    cd raposfly
    docker-compose build

Autostart
~~~~~~~~~

In order to have raposfly starting at boot, we need to create the file
``/etc/systemd/system/raposfly.service`` with the following content:

.. code-block:: cfg

    [Unit]
    Description=raposfly
    Requires=docker.service
    After=docker.service

    [Service]
    Restart=always
    WorkingDirectory=/home/pi/raposfly/
    ExecStart=/usr/local/bin/docker-compose up
    ExecStop=/usr/local/bin/docker-compose down

    [Install]
    WantedBy=default.target

Be sure to change the line ``WorkingDirectory=/home/pi/raposfly/`` with the
current path to the ``raposfly`` folder (user and folder name!).

Then enable the service to start at boot:

.. code-block:: console

    sudo systemctl enable raposfly

Verification
~~~~~~~~~~~~

In order to verify that everything is working correctly, shutdown the Raspberry
Pi:

.. code-block:: console

    sudo shutdown -h now

After the green led has turned off completly, unplug the ethernet cable and the
power cable, and restart the Raspberry Pi by pluging again the power cable (not
the ethernet cable though). With this you would be in a situation that

You should now be able to access the store website by typing ``raposfly.shop`` in
a browser from a client connected through the Wifi!
