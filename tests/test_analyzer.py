from src.engine.analyzer import calculate_risk


class FakeMeta:
    def __init__(self, logs):
        self.log_messages = logs


class FakeTransaction:
    def __init__(self, logs):
        self.meta = FakeMeta(logs)


class FakeTxData:
    def __init__(self, logs):
        self.transaction = FakeTransaction(logs)


def test_low_risk():
    tx = FakeTxData(["random log"])
    level, score = calculate_risk(tx)

    assert level == "LOW 🟢"
    assert score == 0


def test_medium_risk():
    tx = FakeTxData(["Instruction: Transfer"])
    level, score = calculate_risk(tx)

    assert level == "MEDIUM 🟡"
    assert score == 2


def test_high_risk():
    tx = FakeTxData([
        "Instruction: Approve",
        "Instruction: Transfer"
    ])
    level, score = calculate_risk(tx)

    assert level == "HIGH 🔴"
    assert score >= 3


def test_empty():
    level, score = calculate_risk(None)

    assert level == "ERROR"
    assert score == 0