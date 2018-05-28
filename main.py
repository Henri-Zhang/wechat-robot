import itchat
import chat_robot

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
  return chat_robot.get_reply(msg['Text'])

itchat.auto_login()
itchat.run()