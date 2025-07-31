from extremecloudiq.paths.packetcaptures.get import ApiForget
from extremecloudiq.paths.packetcaptures.post import ApiForpost
from extremecloudiq.paths.packetcaptures.delete import ApiFordelete


class Packetcaptures(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
