import pytest
import reverse_sentence


def test1():
    assert "Tadimeti V is name My." == reverse_sentence.reverse(
        "My name is V Tadimeti.")


def test2():
    assert "Hi." == reverse_sentence.reverse("Hi.")


if __name__ == "__main__":
    pytest.main()
