

class MyError(BaseException):
    pass


class Errors:
    @staticmethod
    def test_error(mess: str = "") -> 'MyError':
        return MyError(mess)
