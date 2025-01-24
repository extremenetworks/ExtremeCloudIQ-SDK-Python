from extremecloudiq.paths.radius_servers_internal.get import ApiForget
from extremecloudiq.paths.radius_servers_internal.post import ApiForpost
from extremecloudiq.paths.radius_servers_internal.delete import ApiFordelete


class RadiusServersInternal(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
