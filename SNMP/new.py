from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('localhost',161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr', 0))
)
error_indication, error_status, error_index, var_binds = next(iterator)

# Check for errors and print results
if error_indication:
    print(f"Error: {error_indication}")
else:
    if error_status:
        print('f"Error in response: {error_status}"')
    else:
        for var_bind in var_binds:
            print(f"{var_bind.prettyPrint()}")