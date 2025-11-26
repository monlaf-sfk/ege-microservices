import logging
from vk_bot.loader import bot
from vk_bot.handlers import base_labeler, reg_labeler, scores_labeler

logging.basicConfig(level=logging.INFO)


bot.labeler.load(base_labeler)
bot.labeler.load(reg_labeler)
bot.labeler.load(scores_labeler)

if __name__ == "__main__":
    print("🤖 VK Бот запущен...")
    bot.run_forever()