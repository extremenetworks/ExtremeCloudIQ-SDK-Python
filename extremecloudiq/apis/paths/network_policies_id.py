from extremecloudiq.paths.network_policies_id.get import ApiForget
from extremecloudiq.paths.network_policies_id.put import ApiForput
from extremecloudiq.paths.network_policies_id.delete import ApiFordelete


class NetworkPoliciesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
