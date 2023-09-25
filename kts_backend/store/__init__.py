class Store:
    def __init__(self, app: "Application"):
        from kts_backend.users.accessor import UserAccessor
        from kts_backend.store.bot.manager import BotManager
        from kts_backend.store.vk_api.accessor import VkApiAccessor

        self.user = UserAccessor()
        self.bots_manager = BotManager(app)
        self.vk_api = VkApiAccessor(app)


def setup_store(app: "Application"):
    app.store = Store(app)