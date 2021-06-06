import unittest
import reverse_sentence


class TestCase(unittest.TestCase):
    def test1(self):
        assert "Tadimeti V is name My." == reverse_sentence.reverse(
            "My name is V Tadimeti.")

    def test2(self):
        assert "Hi." == reverse_sentence.reverse("Hi.")


if __name__ == "__main__":
    unittest.main()
