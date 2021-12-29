from os.path import join, dirname

from ovos_plugin_common_play.ocp import MediaType, PlaybackType
from ovos_workshop.skills.common_play import OVOSCommonPlaybackSkill, \
    ocp_search, ocp_featured_media
from youtube_archivist import IAArchivist


class CinemocracySkill(OVOSCommonPlaybackSkill):

    def __init__(self):
        super().__init__("Cinemocracy")
        self.supported_media = [MediaType.GENERIC,
                                MediaType.DOCUMENTARY]
        self.skill_icon = join(dirname(__file__), "ui", "cinemocracy.png")
        self.default_bg = join(dirname(__file__), "ui", "bg.jpeg")
        self.archive = IAArchivist("cinemocracy")

    def initialize(self):
        if len(self.archive.db) == 0:
            # no database, download from url TODO
            self.archive.archive_collection("cinemocracy")

    def match_skill(self, phrase, media_type):
        score = 0
        if self.voc_match(phrase, "cinemocracy", exact=True):
            return 100
        if self.voc_match(phrase, "old"):
            score += 10
        if self.voc_match(phrase, "real"):
            score += 15
        if self.voc_match(phrase, "war"):
            score += 20
        if self.voc_match(phrase, "propaganda"):
            score += 20
        if self.voc_match(phrase, "cinemocracy"):
            score += 50
        return score

    @ocp_search()
    def search_db(self, phrase, media_type):
        score = self.match_skill(phrase, media_type)
        if score >= 50:
            yield {
                "match_confidence": score,
                "media_type": MediaType.DOCUMENTARY,
                "playlist": self.featured_media(),
                "playback": PlaybackType.VIDEO,
                "skill_icon": self.skill_icon,
                "image": self.skill_icon,
                "skill_id": self.skill_id,
                "title": "Cinemocracy",
                "author": "Internet Archive"
            }

    @ocp_featured_media()
    def featured_media(self):
        return [{
                "title": video["title"],
                "image": self.skill_icon,
                "match_confidence": 70,
                "media_type": MediaType.DOCUMENTARY,
                "uri": video["streams"][0],  # TODO format selection
                "playback": PlaybackType.VIDEO,
                "skill_icon": self.skill_icon,
                "skill_id": self.skill_id
            } for _, video in self.archive.db.items() if video.get("streams")]



def create_skill():
    return CinemocracySkill()
