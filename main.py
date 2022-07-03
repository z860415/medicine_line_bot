from src.line import Line
from src.tok import Tok
from datetime import datetime
import datetime as Datetime
import time as Time


if __name__ == "__main__":
    while True:
        time = str(datetime.now()).split('.')[0]
        time_without_date = str(datetime.now()).split('.')[0].split(' ')[1]
        time_date = str(datetime.now()).split('.')[0].split(' ')[0]
        current_time = str(datetime.now() + Datetime.timedelta(minutes=5)).split('.')[0].split(' ')[1][:-3]

        if Tok.is_time_to_take_K_medicine(time_without_date):
            Line.line_Notity_message(f'{current_time} 需餵癲癇藥, 瓶身標註 『 K 』 餵食 1.5cc')
        if Tok.is_time_to_take_P_medicine(time_without_date):
            Line.line_Notity_message(f'{current_time} 需餵癲癇藥, 瓶身標註 『 P 』 餵食 1cc')
        if Tok.is_time_to_eat(time_without_date):
            Line.line_Notity_message(f'{current_time} 需餵飯前藥, 瓶身標註 『 S 』 餵食 2cc')
            Line.line_Notity_message('飯後餵食類固醇, 瓶身標註 『 O 』 餵食 1.5cc')
        if Tok.is_time_to_take_S_medicine(time_without_date):
            Line.line_Notity_message(f'{current_time} 需餵保肝藥, 餵食 1顆')
        print(time)
        Time.sleep(1)
