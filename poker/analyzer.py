import logging.handlers
import sys
from sys import platform

import matplotlib
from poker.scraper.table_setup_actions_and_signals import TableSetupAnalyzeScreenshot

if platform not in ["linux", "linux2"]:
    matplotlib.use('Qt5Agg')

from poker.tools.helper import init_logger


def analyze_screeshot(table_name):
    init_logger(screenlevel=logging.INFO, filename='analyzer', logdir='log')
    log = logging.getLogger("")
    log.info("Initializing program")

    analyzer = TableSetupAnalyzeScreenshot(table_name)
    analyzer.load()

    i = 0
    while True:
        log.info("Analyzing #%s...", i)

        analyzer.take_screenshot()
        analyzer.crop()
        analyzer.test_all()

        log.info("============ DONE =============")
        i += 1


if __name__ == '__main__':
    argv = dict(enumerate(sys.argv))
    analyze_screeshot(argv.get(1) or "Official Poker Stars")
