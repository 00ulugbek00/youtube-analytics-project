import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.youtube = self.get_service()
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file):
        channel_data = {
            'channel_id': self.channel_id,
            'channel_title': self.title,
            'channel_description': self.description,
            'channel_url': self.url,
            'subscriberCount': self.subscriberCount,
            'videoCount': self.video_count,
            'viewCount': self.viewCount
        }
        with open(file, 'w') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)
