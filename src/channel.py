class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_id)
