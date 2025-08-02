from requests import Session
from typing import Optional
from base64 import b64decode, b64encode
from kinescope.const import *
from kinescope.exceptions import *


class KinescopeVideo:
    def __init__(self, url: Optional[str] = None,
                 video_id: Optional[str] = None,
                 referer_url: Optional[str] = None):
        if not (url or video_id):
            raise UrlOrVideoIdRequired('URL or Video Id is required')

        self.url = url
        self.video_id = video_id
        self.referer_url = referer_url

        self.http = Session()

        if not self.video_id:
            self.video_id = self._get_video_id()

    def _get_video_id(self):
        r = self.http.get(
            url=self.url,
            headers={'Referer': self.referer_url}
        )

        if r.status_code == 404:
            raise VideoNotFound('Video not found')

        if 'id: "' not in r.text:
            raise AccessDenied('Access to the video is denied. Wrong referer_url is specified?')

        return r.text.split('id: "')[1].split('"')[0]

    def get_mpd_master_playlist_url(self) -> str:
        return KINESCOPE_MASTER_PLAYLIST_URL.format(video_id=self.video_id)

    def get_clearkey_license_url(self) -> str:
        return KINESCOPE_CLEARKEY_LICENSE_URL.format(video_id=self.video_id)

    def get_license_key(self) -> str:
        try:
            response = self.http.post(
                url=self.get_clearkey_license_url(),
                headers={'origin': KINESCOPE_BASE_URL},
                json={
                    'kids': [
                        b64encode(bytes.fromhex(
                            self._get_cenc_kid()
                        )).decode().replace('=', '')
                    ],
                    'type': 'temporary'
                }
            )
            key = response.json()['keys'][0]['k'] + '=='
            return b64decode(key).hex()
        except KeyError:
            raise UnsupportedEncryption("Unsupported encryption type in this video")

    def _get_cenc_kid(self) -> str:
        # Метод для получения CENC KID из MPD
        # Здесь необходимо достать информацию из MPD о защите контента
        return 'some-cenc-kid'  # Примерное значение, нужно заменить на реальное извлечение из MPD
