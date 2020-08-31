from suntime import Sun
import datetime
from subprocess import Popen, PIPE


class OpenOrCloseDarkMode:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def change_mode(self):
        sun = Sun(self.latitude, self.longitude)
        sunrise = '''
                    tell application "System Events"
                        tell appearance preferences
                            set dark mode to false
                        end tell
                    end tell
                    '''
        sunset = '''
            tell application "System Events"
                        tell appearance preferences
                            set dark mode to true
                        end tell
                    end tell
        
        '''
        p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        today_sr = (sun.get_sunrise_time() - datetime.timedelta(hours=16)).strftime('%Y-%m-%d %H:%M')
        today_ss = (sun.get_sunset_time() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
        print(today_sr, today_ss)
        # 获取当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        # 白天（不需要开暗黑模式）
        if today_sr < now < today_ss:
            p.communicate(sunrise)
        else:
            p.communicate(sunset)
        return


if __name__ == '__main__':
    latitude = 23.02882
    longitude = 113.14278
    OpenOrCloseDarkMode(latitude, longitude).change_mode()
