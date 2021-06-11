from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests

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
    def testcon(self, message, service=None):
        """This function is just for connection testing."""

        return "This is working. You have successfully installed Selenium automated testing plugin."