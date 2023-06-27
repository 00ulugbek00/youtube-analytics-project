import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        self.__youtube = self.get_service()
        self.__channel = self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.__subscriberCount = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__viewCount = self.__channel['items'][0]['statistics']['viewCount']

    def __str__(self) -> str:
        return f'{self.__title} ({self.__url})'

    def __eq__(self, other) -> bool:
        """
        Проверяет, равен ли данный объект Channel
        """

        return self.__subscriberCount == other.__subscriberCount

    def __le__(self, other) -> bool:
        """__le__(self, other) — определяет поведение оператора сравнения «меньше или равно», <=.
         """
        return self.__subscriberCount <= other.__subscriberCount

    def __ge__(self, other) -> bool:
        """  __ge__(self, other) — определяет поведение оператора сравнения «больше или равно», >=.
        """
        return self.__subscriberCount >= other.__subscriberCount

    def __gt__(self, other) -> bool:
        """__gt__(self, other) — определяет поведение оператора сравнения «больше», >.
        """
        return self.__subscriberCount > other.__subscriberCount

    def __lt__(self, other) -> bool:
        """
        Проверяет, является ли данный объект Channel меньшим
        """
        return self.__subscriberCount < other.__subscriberCount

    def __add__(self, other):
        """
    	Метод срабатывает, когда используется оператор сложения.
    	    В параметре other хранится то, что справа от знака +
        """
        return other.__subscriberCount + self.__subscriberCount

    def __rsub__(self, other) -> int:
        """
        Вычитает количество подписчиков данного объекта Channel
        """
        return self.__subscriberCount - other.__subscriberCount

    def __sub__(self, other) -> int:
        """
        Вычитает количество подписчиков другого объекта Channel
        """
        return self.__subscriberCount - other.__subscriberCount

    @property
    def channel_id(self) -> str:
        """
         Идентификатора YouTube-канала.
         """
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel, indent=2, ensure_ascii=False))

    def to_json(self, file):
        channel_data = {
            'channel_id': self.__channel_id,
            'channel_title': self.__title,
            'channel_description': self.__description,
            'channel_url': self.__url,
            'subscriberCount': self.__subscriberCount,
            'videoCount': self.__video_count,
            'viewCount': self.__viewCount
        }
        with open(file, 'w') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)
