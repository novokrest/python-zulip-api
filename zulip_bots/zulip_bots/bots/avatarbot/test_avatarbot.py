from zulip_bots.test_lib import BotTestCase

class TestHelpBot(BotTestCase):
    bot_name = "avatarbot"  # type: str

    def test_bot(self) -> None:
        self.assertTrue(True)
