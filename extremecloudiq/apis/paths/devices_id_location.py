from extremecloudiq.paths.devices_id_location.get import ApiForget
from extremecloudiq.paths.devices_id_location.put import ApiForput
from extremecloudiq.paths.devices_id_location.delete import ApiFordelete


class DevicesIdLocation(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
