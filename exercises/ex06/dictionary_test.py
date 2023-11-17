"""Testing dictionary exercise."""

__author__ = "730525294"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_usecases() -> None:
    """Testing invert function in use cases."""
    assert invert({"a": "1", "b": "2", "c": "3"})


def test_invert_usecases1() -> None:
    """Testing invert function in use cases."""
    assert invert({"ae": "1a", "be": "2a", "ce": "3a"})


def test_invert_edgecase() -> None:
    """Testing invert function in edge cases."""
    assert invert({"a": "a", "be": "a1", "e": "e"})


def test_favorite_color_usecases() -> None:
    """Testing favorite_color function in use cases."""
    assert favorite_color({"Michael": "blue", "Mike": "blue", "Jerry": "red"})


def test_favorite_color_usecases1() -> None:
    """Testing favorite_color function in use cases."""
    assert favorite_color({"Michael": "yellow", "Michelle": "blue", "Tom": "purple", "Kemeng": "purple"})


def test_favorite_color_edgecase() -> None:
    """Testing favorite_color function in edge cases."""
    assert favorite_color({"Michael": "blue", "Mike": "blue", "Jerry": "red", "Tom": "red"})


def test_count_usecases() -> None:
    """Testing count function in use cases."""
    assert count(["a", "a", "b", "a"])


def test_count_usecases1() -> None:
    """Testing count function in use cases."""
    assert count(["Michael", "Michelle", "Michael", "Tom"])


def test_count_edgecase() -> None:
    """Testing count function in edge cases."""
    assert count(["Michael", "Tom", "Jerry"])


def test_alphabetizer_usecases() -> None:
    """Testing alphabetize function in use cases."""
    assert alphabetizer(["banana", "apple", "peanut", "appendix"])


def test_alphabetizer_usecases1() -> None:
    """Testing alphabetize function in use cases."""
    assert alphabetizer(["good", "better", "affection", "boy", "great"])


def test_alphabetizer_edgecase() -> None:
    """Testing alphabetize function in edge cases."""
    assert alphabetizer(["Party", "play", "affection", "Apple"])


def test_update_attendance_usecases() -> None:
    """Testing update_attendance function in use cases."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Michael"], "Tuesday": ["Tom"]}
    assert update_attendance(attendance_log, "Monday", "Jerry")


def test_update_attendance_usecases1() -> None:
    """Testing update_attendance function in use cases."""
    attendance_log: dict[str, list[str]] = {"Wednesday": ["Michelle"], "Thursday": ["Vrinda"]}
    assert update_attendance(attendance_log, "Thursday", "Elizabeth")


def test_update_attendance_usecase2() -> None:
    """Testing update_attendance function in use cases."""
    attendance_log: dict[str, list[str]] = {"Wednesday": ["Michelle"], "Thursday": ["Vrinda"]}
    assert update_attendance(attendance_log, "Friday", "Elizabeth")


def test_update_attendance_edgecase() -> None:
    """Testing update_attendance function in edge cases."""
    attendance_log: dict[str, list[str]] = {"Wednesday": ["Michelle"], "Friday": ["Vrinda"]}
    assert update_attendance(attendance_log, "Wednesday", "Michelle")