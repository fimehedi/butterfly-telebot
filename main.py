from module.bot import Bot, config
from module.code_runner import CodeRunner


# Start Command
@Bot.message_handler(commands=['start'])
def start(message):
    Bot.reply_to(message, config['START'])

# # Help Command
@Bot.message_handler(commands=['help'])
def help(message):
    Bot.reply_to(message, config['HELP'])

# # Code Run Command
@Bot.message_handler(commands=['run'])
def run(message):
    code = message.reply_to_message.text
    language = message.text.split('.')[1]
    response = CodeRunner(code, language)
    reply = f"\nOutput : ⬇\n{response['output']}\nCPU Time : {response['cpuTime']} | Memory : {response['memory']}"
    Bot.reply_to(message, reply)

# # Check Mention
def is_mention(message):
    request = message.text
    if 'butterfly' in request.lower() or request == '@butterfly_lpibot':
        return True
    return False

# Mention Feedback
@Bot.message_handler(func=is_mention)
def send_mention_reply(message):
    if '@butterfly_lpibot' in message.text:
        Bot.reply_to(message, 'Hey There! I\'m here. 👋')
    else:
        Bot.reply_to(message, 'Thanks for remembering! 😍')


if __name__ == '__main__':
    Bot.polling(none_stop=True)