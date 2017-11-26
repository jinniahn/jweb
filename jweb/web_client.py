'''\

WebClient

  - create selenium driver to run command on browser
  - web client create browser by rpyc
'''

import os.path
import rpyc

from pprint import pprint

curdir = os.path.abspath(os.path.dirname(__file__))

class WebClient(object):
    ''' web client '''
    
    def __init__(self):
        self.conn = rpyc.classic.connect('localhost')
        self.selenium = self.conn.modules['selenium']
        self.ui = self.conn.modules['selenium.webdriver.support.ui']
        self.driver = self._getWebDriver()        

    def _createDriver(self):
        'create selenium dirver'

        lines = '''\
        import selenium
        from selenium import webdriver
        selenium.cur_driver = webdriver.Chrome()
        '''
        for l in lines.splitlines():
            l = l.strip()
            self.conn.execute(l)

        driver = self.conn.modules.selenium.cur_driver
        return driver

    def _getWebDriver(self):
        try:
            driver = self.conn.modules.selenium.cur_driver
        except Exception as e:
            return self._createDriver()

        try:
            driver.current_url
        except Exception as e:
            return self._createDriver()
        return driver

    def run_js(self, code, jquery=True):
        '''run javascript code'''

        if jquery:
            jscode = 'return window["jQuery"] != undefined'
            is_existed = self.driver.execute_script(jscode)
        
            if not is_existed:
                jscode = open(os.path.join(curdir,'data/jquery.js')).read()
                self.driver.execute_script(jscode)

        return self.driver.execute_script(code)

    def get(self, url):
        self.driver.get(url)
