from extremecloudiq.paths.locations_floor_id.get import ApiForget
from extremecloudiq.paths.locations_floor_id.put import ApiForput
from extremecloudiq.paths.locations_floor_id.delete import ApiFordelete


class LocationsFloorId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
