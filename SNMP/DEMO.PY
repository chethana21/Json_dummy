# from pysnmp.entity import engine, config
# from pysnmp.entity.rfc3413 import cmdrsp, context
# from pysnmp.proto import rfc1902
# from pyasn1.type import univ
# from pysnmp.carrier.asynsock.dgram import udp
# from pysnmp.entity.rfc3413.oneliner import ntforg, ntforg

# # Create SNMP engine
# snmpEngine = engine.SnmpEngine()

# # Define a custom OID
# customOID = univ.ObjectIdentifier((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 0))

# # Create a Managed Object
# mibBuilder = snmpEngine.msgAndPduDsp.mibInstrumController.mibBuilder
# mibBuilder.exportSymbols('1.3.6.1.2.1.99.1.1.1.0', customOID)

# def read_handler(oid, tag):
#     if oid == customOID:
#         return rfc1902.Integer(1234)
#     return rfc1902.Integer(0)  # Return 0 for other OIDs

# # Register the read_handler function as a callback for GET requests
# snmpContext = context.SnmpContext(snmpEngine)

# # Define a context for your simulator
# snmpContext.registerContextName('simulator')
# snmpContext.getMibInstrum().getPduAndContext = lambda k: (read_handler, 'simulator')

# # Define the SNMP community
# config.addV1System(snmpEngine, 'my-community', 'public')

# # Bind the SNMP engine to the UDP interface and port
# config.addTransport(
#     snmpEngine,
#     udp.domainName,  # or udp6.domainName for IPv6
#     udp.UdpSocketTransport().openServerMode(('127.0.0.1', 161))
# )

# config.addV1System(snmpEngine, 'my-area', 'public')
# config.addVacmUser(snmpEngine, 1, 'my-area', 'noAuthNoPriv', (1, 3, 6))

# # Start the SNMP engine
# snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

# try:
#     print("SNMP simulator is running...")
#     snmpEngine.transportDispatcher.runDispatcher()
# except KeyboardInterrupt:
#     snmpEngine.transportDispatcher.closeDispatcher()

# from pysnmp.hlapi import *

# # SNMP parameters
# target_ip = '192.168.1.1'
# target_port = 161
# community_string = 'public'
# oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

# # Create an SNMP request
# snmp_engine = SnmpEngine()
# get_cmd = getCmd(snmp_engine,
#                  CommunityData(community_string),
#                  UdpTransportTarget((target_ip, target_port)),
#                  ContextData(),
#                  oid)

# # Execute the request
# error_indication, error_status, error_index, var_binds = next(get_cmd)

# # Check for errors and print results
# if error_indication:
#     print(f"Error: {error_indication}")
# else:
#     if error_status:
#         print(f"Error in response: {error_status}")
#     else:
#         for var_bind in var_binds:
#             print(f"{var_bind.prettyPrint()}")

# # Cleanup
# snmp_engine.transportDispatcher.closeDispatcher()

# from pysnmp.hlapi import *

# # SNMP parameters
# target_ip = 'demo.snmplabs.com'
# target_port = 161  # Default SNMP port
# community_string = 'public'  # Community string for the public test agent
# oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

# # Create an SNMP request
# snmp_engine = SnmpEngine()
# get_cmd = getCmd(
#     snmp_engine,
#     CommunityData(community_string),
#     UdpTransportTarget((target_ip, target_port)),
#     ContextData(),
#     oid
# )

# # Execute the request
# error_indication, error_status, error_index, var_binds = next(get_cmd)

# # Check for errors and print results
# if error_indication:
#     print(f"Error: {error_indication}")
# else:
#     if error_status:
#         print(f"Error in response: {error_status}")
#     else:
#         for var_bind in var_binds:
#             print(f"{var_bind.prettyPrint()}")

# # Cleanup
# snmp_engine.transportDispatcher.closeDispatcher()
