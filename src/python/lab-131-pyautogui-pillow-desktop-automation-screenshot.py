#
# filename    : lab-131-pyautogui-pillow-desktop-automation-screenshot.py
# Description : Desktop automation
# Docs        :
#               * https://pypi.org/project/PyAutoGUI/
#               * https://pyautogui.readthedocs.io/en/latest/quickstart.html
# Requirements:
#               * pip install pyautogui
#               * pip install pillow
#

import pyautogui
import os
from time import sleep

STARTUP_APP = 'C:/Program Files (x86)/Microsoft SQL Server/120/Tools/Binn/ManagementStudio/Ssms.exe'
SERVERNAME_APP = 'LP1764\SQLEXPRESS'
USERNAME_APP = 'sre_user'
PASSWORD_APP = 'sre_user'
QUERY_APP = 'SELECT * FROM INFORMATION_SCHEMA.TABLES'

SCREENSHOT_FILENAME_PREFIX = 'screenshoot-'
SCREENSHOT_EXTENSION_SUFIX = '.png'

IMG_DLGBOX_LOGIN = 'resources/img-ssms-dlgbox-login.png'
IMG_BTN_CONNECT = 'resources/img-ssms-btn-connect.png'
IMG_BTN_CANCEL = 'resources/img-ssms-btn-cancel.png'
IMG_ICON_COLLAPSED_DATABASE = 'resources/img-ssms-icon-collapsed-database.png'
IMG_ICON_NEW_QUERY = 'resources/img-ssms-icon-new-query.png'
IMG_ICON_EXECUTE_QUERY = 'resources/img-ssms-icon-execute-query.png'
IMG_MENU_FILE = 'resources/img-ssms-menu-file.png'
IMG_MENU_FILE_EXIT = 'resources/img-ssms-menu-file-exit.png'

#
# __main__:
#

if __name__ == '__main__':

    # Startup application ...
    os.startfile(STARTUP_APP)

    # Wait for login ...
    sleep(5)

    # Login: servername, Username, Password and connect
    location = pyautogui.locateOnScreen(IMG_DLGBOX_LOGIN)
    print('login - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left, location.top)
        pyautogui.click()
    if SERVERNAME_APP != '':
        pyautogui.write(SERVERNAME_APP)
    pyautogui.press('tab')
    pyautogui.press('tab')
    if USERNAME_APP != '':
        pyautogui.write(USERNAME_APP)
    pyautogui.press('tab')
    if PASSWORD_APP != '':
        pyautogui.write(PASSWORD_APP)
    location = pyautogui.locateOnScreen(IMG_BTN_CONNECT)
    print('connect button - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
    img = pyautogui.screenshot()
    img.save(SCREENSHOT_FILENAME_PREFIX + '01-login' + SCREENSHOT_EXTENSION_SUFIX)
    pyautogui.click()

    # Wait for Logged In  ...
    sleep(2)
    img = pyautogui.screenshot()
    img.save(SCREENSHOT_FILENAME_PREFIX + '02-logged-in' + SCREENSHOT_EXTENSION_SUFIX)

    # Expand database
    location = pyautogui.locateOnScreen(IMG_ICON_COLLAPSED_DATABASE)
    print('expand database - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        pyautogui.doubleClick()

    # New Query  ...
    sleep(1)
    location = pyautogui.locateOnScreen(IMG_ICON_NEW_QUERY)
    print('new query - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        pyautogui.click()
        pyautogui.write(QUERY_APP)

    # Execute Query  ...
    pyautogui.moveTo(1, 1)
    sleep(1)
    location = pyautogui.locateOnScreen(IMG_ICON_EXECUTE_QUERY)
    print('Execute query - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        pyautogui.click()
    sleep(1)
    img = pyautogui.screenshot()
    img.save(SCREENSHOT_FILENAME_PREFIX + '03-query-result' + SCREENSHOT_EXTENSION_SUFIX)

    # File >> Exit  ...
    sleep(2)
    location = pyautogui.locateOnScreen(IMG_MENU_FILE)
    print('Menu File - location:', location)
    if location is not None:
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        pyautogui.click()
        sleep(1)
        location = pyautogui.locateOnScreen(IMG_MENU_FILE_EXIT)
        print('Menu File - location:', location)
        if location is not None:
            pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        pyautogui.click()
        sleep(1)
        pyautogui.write('N')
