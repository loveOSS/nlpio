from nlptools.nlptools import strip_html_tags


class TestNlptools():
    """Tests about NLP Tools"""

    def test_simple_markup(self):
        title = '<h1>Hello World</h1>'
        assert 'Hello World' == strip_html_tags(title)

    def test_double_markup(self):
        complex_html = '<div><p>Hello World</p></div>'
        assert 'Hello World' == strip_html_tags(complex_html)

    def test_complex_markup(self):
        link = '<a href="*">Hello World</a>'
        assert 'Hello World' == strip_html_tags(link)
