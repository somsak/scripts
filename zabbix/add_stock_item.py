#!/usr/bin/env python

import sys
from zabbix_api import ZabbixAPI

server="http://localhost/zabbix"
username="admin"
password="password"

if len(sys.argv) < 3 :
    print 'Usage: %s <Host name> <symbol1> [symbol2] [symbol3]...'
    sys.exit(1)

zapi = ZabbixAPI(server=server, path="", log_level=0)
zapi.login(username, password)

host_name=sys.argv[1]

host_id = zapi.host.get({"filter":{"host":host_name}})[0]["hostid"]

interface_id = zapi.hostinterface.get({"hostids":host_id, "output":"extend"})[0]["interfaceid"]

#[{u'itemid': u'23432', u'username': u'', u'inventory_link': u'0', u'lastclock': u'1364049636', u'lastlogsize': u'0', u'trends': u'365', u'snmpv3_authpassphrase': u'', u'snmp_oid': u'', u'templateid': u'0', u'snmpv3_securitylevel': u'0', u'port': u'', u'multiplier': u'0', u'lastns': u'279613233', u'authtype': u'0', u'password': u'', u'logtimefmt': u'', u'mtime': u'0', u'delay': u'3600', u'publickey': u'', u'params': u'', u'snmpv3_securityname': u'', u'formula': u'1', u'type': u'10', u'prevvalue': u'0', u'status': u'3', u'lastvalue': u'0', u'snmp_community': u'', u'description': u'', u'data_type': u'0', u'trapper_hosts': u'', u'units': u'THB', u'value_type': u'0', u'prevorgvalue': u'0', u'delta': u'0', u'delay_flex': u'300/1-5,08:00-16:30', u'lifetime': u'30', u'interfaceid': u'1', u'snmpv3_privpassphrase': u'', u'hostid': u'10085', u'key_': u'stock_price.py["CITY"]', u'name': u'Last Price of CITY', u'privatekey': u'', u'filter': u'', u'valuemapid': u'0', u'flags': u'0', u'error': u'Received value [4.1] is not suitable for value type [Numeric (unsigned)] and data type [Decimal]', u'ipmi_sensor': u'', u'history': u'90'}]

for symbol in sys.argv[2:] :
    zapi.item.create( {
        'hostid': host_id,
        'description': '',
        'type':10,
        'value_type':0,
        'interfaceid': interface_id, 
        'key_': 'stock_price.py["-f", "last", %s]' % (symbol), 
        'trends': 365, 
        'delay': 21600, 
        'units': 'THB', 
        'delay_flex': '60/1-5,09:55-12:30;60/1-5,14:25-16:35',
        'lifetime': 30, 
        'name': 'Last Price of %s' % (symbol), 
        'flags': 4, 
        'history': 90,
    })
