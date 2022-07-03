import requests
import os

class Line:
    def line_Notity_message(message):
        line_headers = {
            "Authorization": "Bearer " + os.getenv('TOKEN'),
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {'message': message}

        print(os.getenv('TOKEN'))

        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=line_headers, params=params)

        return r.status_code
