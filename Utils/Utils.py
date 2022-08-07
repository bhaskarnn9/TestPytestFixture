import sys
from get_project_root import root_path


class Utils:

    @staticmethod
    def take_screenshot(driver):
        caller_name = sys._getframe().f_back.f_code.co_name
        path = f'{root_path(ignore_cwd=True)}/Screenshots'
        print('caller_name', caller_name)
        driver.save_screenshot(f'{path}/{caller_name}.png')
