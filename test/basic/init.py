import sys

from SingleLog.log import Logger

import PyPtt


def func():
    logger.info('===預設值===')
    PyPtt.API()
    logger.info('===中文顯示===')
    PyPtt.API(language=PyPtt.Lang.CHINESE)
    logger.info('===英文顯示===')
    PyPtt.API(language=PyPtt.Lang.ENGLISH)
    logger.info('===log DEBUG===')
    PyPtt.API(log_level=PyPtt.LOG_LEVEL.DEBUG)
    logger.info('===log INFO===')
    PyPtt.API(log_level=PyPtt.LOG_LEVEL.INFO)
    logger.info('===log SLIENT===')
    PyPtt.API(log_level=PyPtt.LOG_LEVEL.SILENT)
    logger.info('===log SLIENT======')

    ptt_bot = PyPtt.API(host=PyPtt.HOST.PTT1)
    logger.info('host', ptt_bot.host)

    ptt_bot = PyPtt.API(host=PyPtt.HOST.PTT2)
    logger.info('host', ptt_bot.host)

    try:
        logger.info('===語言 99===')
        PyPtt.API(language=99)
    except TypeError:
        logger.info('通過')
    except:
        logger.info('沒通過')
        assert False
    logger.info('===語言放字串===')
    try:
        PyPtt.API(language='PyPtt.i18n.language.ENGLISH')
    except TypeError:
        logger.info('通過')
    except:
        logger.info('沒通過')
        assert False



    # def handler(msg):
    #     with open('log.txt', 'a', encoding='utf-8') as f:
    #         f.write(msg + '\n')
    #
    #
    # ptt_bot = PyPtt.API(
    #     log_handler=handler)
    # logger.info('Test log')

    logger.info('complete')


if __name__ == '__main__':
    logger = Logger('TEST INIT')
    func()
