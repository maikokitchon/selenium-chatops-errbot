from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests
import os
import sys
sys.path.insert(0, '.' + os.path.dirname(os.path.abspath(__file__)))
from lib.login import Login

class Selenium(BotPlugin):
    """
    selenium
    """
    _services = {
        'selenium_webdriver': {
            'url': ''
        },
    }

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(Selenium, self).activate()

    @botcmd
    def selenium_testcon(self, message, service=None):
        """This function is just for connection testing."""

        return "This is working. You have successfully installed Selenium automated testing plugin."

    @botcmd
    def selenium_test_osc_login(self, message, service=None):
        """This function is to run automated login testing in Opensource CMS."""
        # WORK_DIR = os.getcwd()
        # THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
        # print('WORK_DIR', WORK_DIR)
        # print('THIS_FILE_DIR', THIS_FILE_DIR)
        frm = message.frm
        
        x = Login()
        result = x.execute_test()

        resp = "| key      | value\n"
        resp += "| -------- | --------\n"
        resp += f"| Triggered By | `{frm.person}`\n"
        resp += f"| Test Module | Login\n"
        resp += f"| Test Logs| {result}\n"

        return resp