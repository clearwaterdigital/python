import logging

logger = logging.getLogger(__name__)

import time
import cwutils.cwlogging


def run():
    
    for i in range(5):
        logger.info('and i is now {}'.format(i))
        time.sleep(3)



if __name__ == '__main__':

    cwutils.cwlogging.configureStandaloneLogging()
    cwutils.cwlogging.addLogDNAHandler()
    logger.info('using logdna')
    run()