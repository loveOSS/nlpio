from nlpio.nlpio import (
    strip_html_tags,
    replace_accented_chars,
    remove_special_characters,
    clean_corpus,
)


class TestNlptools:
    """Tests about NLP Tools"""

    def test_simple_markup(self):
        title = "<h1>Hello World</h1>"
        assert "Hello World" == strip_html_tags(title)

    def test_double_markup(self):
        complex_html = "<div><p>Hello World</p></div>"
        assert "Hello World" == strip_html_tags(complex_html)

    def test_complex_markup(self):
        link = '<a href="*">Hello World</a>'
        assert "Hello World" == strip_html_tags(link)

    def test_invalid_markup(self):
        invalid_link = '<a href="*">Hello World<a>'
        assert "Hello World" == strip_html_tags(invalid_link)

    def test_replace_accented_chars(self):
        sentence = "àáäçéèëíïóúýñÁÉÍÓÚÝ"
        assert "aaaceeeiiouynAEIOUY" == replace_accented_chars(sentence)

    def test_remove_special_chars(self):
        special_char = "This is my intent©"
        assert "This is my intent" == remove_special_characters(special_char)

    def test_remove_emojis(self):
        emoji_sentence = "Hi everyone, how are you ? 🙂"
        assert "Hi everyone how are you  " == remove_special_characters(emoji_sentence)

    def test_remove_punctuation(self):
        punctuation_sentence = "Hi; everyone - except you ?"
        assert "Hi everyone  except you " == remove_special_characters(
            punctuation_sentence
        )

    def test_remove_punctuation_and_numbers(self):
        complex_sentence = "How old is she ? She is 17 years old"
        assert "How old is she  She is  years old" == remove_special_characters(
            complex_sentence, True
        )

    def test_clean_corpus(self):
        corpus = ["Hi; everyone - except you ?", "<h1>Hello</h1>", "This is my intent©"]

        cleaned_corpus = ["hi everyone except", "hello", "intent"]

        assert cleaned_corpus == clean_corpus(corpus)
