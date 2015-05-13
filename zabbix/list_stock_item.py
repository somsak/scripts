#!/usr/bin/env python

import sys
from zabbix_api import ZabbixAPI

server="http://localhost/zabbix"
username="admin"
password="password"

if len(sys.argv) < 2 :
    print 'Usage: %s <Host name>' % (sys.argv[0])
    sys.exit(1)

zapi = ZabbixAPI(server=server, path="", log_level=0)
zapi.login(username, password)

host_name=sys.argv[1]

host_id = zapi.host.get({"filter":{"host":host_name}})[0]["hostid"]
for item in zapi.item.get({"hostids":host_id, "output":"extend"}) :
    print item
