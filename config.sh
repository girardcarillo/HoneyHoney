#Check if package is installed, if no --> install
if [ $(dpkg-query -W -f='${Status}' python-paho-mqtt 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt-get install -y python-paho-mqtt;
fi

#Cleanup & rewrite rc.local
sudo rm /etc/rc.local

sudo echo "#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi


# Run Python script for HoneyHoney project on booting

sudo python /home/pi/HoneyHoney/HoneyHoney.py

exit 0" > /etc/rc.local
