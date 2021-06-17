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

        self.send(message.frm, 'I am now executing a test. Please wait...')

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
                        thumbnail='/chatbot/data/plugins/maikokitchon/selenium-chatops-errbot/lib/output/1-login-form.png',
                        image='/chatbot/data/plugins/maikokitchon/selenium-chatops-errbot/lib/output/1-login-form.png',
                        fields=(('First Key','Value1'), ('Second Key','Value2')),
                        color='red',
                        in_reply_to=message
        )

        self.send_stream_request(message.frm, open('/chatbot/data/plugins/maikokitchon/selenium-chatops-errbot/lib/output/1-login-form.png', 'r'), name='login-form.png')

        return resp