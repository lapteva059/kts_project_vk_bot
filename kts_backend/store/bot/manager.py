import typing

from kts_backend.store.vk_api.dataclasses import Update, Message

if typing.TYPE_CHECKING:
    from kts_backend.web.app import Application


class BotManager:
    def __init__(self, app: "Application"):
        self.app = app
        self.bot = None

    async def start(self):
        pass
    async def get_game_by_chat_id(self):
        pass
    async def send_message(self):
        pass
    async def update_message(self):
        pass
    async def check_update(self):
        pass
    async def finish_game(self):
        pass

    async def handle_updates(self, updates: list[Update]):
        for update in updates:
            await self.app.store.vk_api.send_message(
                Message(
                    user_id=update.object.message.id,
                    text=update.object.message.text
                )
            )