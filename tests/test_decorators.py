from src.decorators import log


def test_decorators():
    @log(filename="log.txt")
    def sum_(x, y):
        return x + y

    decorator_1 = sum_(3, 4)
    assert decorator_1 == 7


def test_capsys_decorators(capsys) -> None:
    @log()
    def sum_(x, y):
        return x + y

    sum_(6, 2)
    read_out = capsys.readouterr()
    assert read_out.out == "sum_ OK\n\n"


def test_decorators_error(capsys) -> None:
    @log()
    def sum_(x, y):
        return x + y

    sum_(6, "2")
    read_out = capsys.readouterr()
    assert read_out.out == "sum_ error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (6, '2'), {}\n\n"
