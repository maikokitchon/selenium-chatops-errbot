from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests
# sys.path.insert(0, '.' + os.path.dirname(os.path.abspath(__file__)))
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/lib")
from login import Login

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

        # resp = "| key      | value\n"
        # resp += "| -------- | --------\n"
        # resp += f"| Triggered By | `{frm.person}`\n"
        # resp += f"| Test Module | Login\n"

        resp = "Triggered By: " + frm.person + "\n"
        resp += "Automated test log result: \n ```" + result

        self.send_card( title='Title + Body',
                        body='text body to put in the card',
                        thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
                        image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                        link='http://www.google.com',
                        fields=(('First Key','Value1'), ('Second Key','Value2')),
                        color='red',
                        in_reply_to=message
        )

        return resp