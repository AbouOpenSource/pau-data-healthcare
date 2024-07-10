

import paho.mqtt.publish as publish

data = 22.0

publish.single("temperature", data, hostname="240e633499364315936f402251fc1490.s1.eu.hivemq.cloud")