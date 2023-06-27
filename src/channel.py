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
        self.subscriberCount = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self) -> str:
        return f'{self.title} ({self.url})'

    def __eq__(self, other) -> bool:
        """
        Проверяет, равен ли данный объект Channel
        """

        return self.subscriberCount == other.subscriberCount

    def __le__(self, other) -> bool:
        """__le__(self, other) — определяет поведение оператора сравнения «меньше или равно», <=.
         """
        return self.subscriberCount <= other.subscriberCount

    def __ge__(self, other) -> bool:
        """  __ge__(self, other) — определяет поведение оператора сравнения «больше или равно», >=.
        """
        return self.subscriberCount >= other.subscriberCount

    def __gt__(self, other) -> bool:
        """__gt__(self, other) — определяет поведение оператора сравнения «больше», >.
        """
        return self.subscriberCount > other.subscriberCount

    def __lt__(self, other) -> bool:
        """
        Проверяет, является ли данный объект Channel меньшим
        """
        return self.subscriberCount < other.subscriberCount

    def __add__(self, other) -> int:
        """
        Складывает количество подписчиков данного объекта Channel"""
        return self.subscriberCount + other.subscriberCount

    def __rsub__(self, other) -> int:
        """
        Вычитает количество подписчиков данного объекта Channel
        """
        return other.self.subscriberCount - self.subscriberCount

    def __sub__(self, other) -> int:
        """
        Вычитает количество подписчиков другого объекта Channel
        """
        return self.subscriberCount - other.subscriberCount

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
