from extremecloudiq.paths.ldap_servers_id.get import ApiForget
from extremecloudiq.paths.ldap_servers_id.put import ApiForput
from extremecloudiq.paths.ldap_servers_id.delete import ApiFordelete


class LdapServersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
