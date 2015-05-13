#!/usr/bin/env python

import sys
from zabbix_api import ZabbixAPI

server="http://www.thaipbs.or.th/zabbix"
username="admin"
password="tpbsmonitoring"

zapi = ZabbixAPI(server=server, path="", log_level=0)
zapi.login(username, password)

host_name = sys.argv[1]

#host_id = zapi.trigger.get({"filter":{"host":host_name}})[0]["hostid"]
host_id = zapi.trigger.get({"filter":{"host":host_name}, "output":"extend"})
print host_id
#for item in zapi.trigger.get({"hostids":host_id, "output":"extend"}) :
#    print item
