#!/bin/bash

ln -s /mnt/data/etc/wb-location-settings/wb-locations-settings.schema.json /usr/share/wb-mqtt-confed/schemas/wb-locations-settings.schema.json

service wb-mqtt-confed restart
