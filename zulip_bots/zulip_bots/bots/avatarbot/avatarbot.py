# See readme.md for instructions on running this code.

from typing import Any

import os

class AvatarBotHandler(object):
    def usage(self) -> str:
        return '''
        This is a boilderplate bot that can change own avatar to image on user's local machine.
        Specify the avatar path you want to set for the bot and bot changes own avatar.'
        '''

    def handle_message(self, message: Any, bot_handler: Any) -> None:
        HELP_STR = (
            'Mention the avatar bot in a conversation and '
            'then enter path of any file you want to set as bot\'s avatar'
        )

        content = message['content'].strip()  # type: str
        if content == '' or content == 'help':
            bot_handler.send_reply(message, HELP_STR)
            return

        path = content
        if not os.path.isfile(path):
            bot_handler.send_reply(message, 'Could not find `{}` file'.format(path))
            return
        res = bot_handler.upload_avatar(path)
        if res['result'] != 'success':
            bot_handler.send_reply(message, 'Error occurred while uploading avatar: {}'.format(res['msg']))
        else:
            bot_handler.send_reply(message, '[avatar]({})'.format(res['avatar_url']))

handler_class = AvatarBotHandler
