from datetime import datetime


class Tok:
    __K = ["23:55:00", "07:55:00", "15:55:00"]
    __P = ["07:55:00", "19:55:00"]
    __S = ["21:55:00"]

    def is_time_to_take_K_medicine(time_without_date):
        if time_without_date in Tok.__K:
            return True

    def is_time_to_take_P_medicine(time_without_date):
        if time_without_date in Tok.__P:
            return True

    def is_time_to_eat(time_without_date):
        if time_without_date in ["07:25:00", "16:25:00"]:
            return True

    def is_time_to_take_S_medicine(time_without_date):
        if time_without_date in Tok.__S:
            return True

