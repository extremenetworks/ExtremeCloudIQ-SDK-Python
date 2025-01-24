from extremecloudiq.paths.devices_id_network_policy.get import ApiForget
from extremecloudiq.paths.devices_id_network_policy.put import ApiForput
from extremecloudiq.paths.devices_id_network_policy.delete import ApiFordelete


class DevicesIdNetworkPolicy(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
