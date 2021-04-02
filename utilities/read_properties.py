import configparser

config = configparser.RawConfigParser()
config.read("Config\\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def getFromYear():
        from_year = config.get("leave info", "fromYear")
        return from_year

    @staticmethod
    def getFromMonth():
        from_month = config.get("leave info", "fromMonth")
        return from_month

    @staticmethod
    def getFromDate():
        from_date = config.get("leave info", "fromDate")
        return from_date

    @staticmethod
    def getToYear():
        to_year = config.get("leave info", "toYear")
        return to_year

    @staticmethod
    def getToMonth():
        to_month = config.get("leave info", "toMonth")
        return to_month

    @staticmethod
    def getToDate():
        to_date = config.get("leave info", "toDate")
        return to_date

    @staticmethod
    def getUnit():
        unit = config.get("leave info", "unit")
        return unit