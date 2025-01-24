from extremecloudiq.paths.vlan_profiles_id.get import ApiForget
from extremecloudiq.paths.vlan_profiles_id.delete import ApiFordelete
from extremecloudiq.paths.vlan_profiles_id.patch import ApiForpatch


class VlanProfilesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
