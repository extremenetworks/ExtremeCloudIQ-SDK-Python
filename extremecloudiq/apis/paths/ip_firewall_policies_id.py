from extremecloudiq.paths.ip_firewall_policies_id.get import ApiForget
from extremecloudiq.paths.ip_firewall_policies_id.put import ApiForput
from extremecloudiq.paths.ip_firewall_policies_id.delete import ApiFordelete


class IpFirewallPoliciesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
