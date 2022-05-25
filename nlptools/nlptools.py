import unicodedata
import re
import nltk
import spacy

from bs4 import BeautifulSoup
from nltk.tokenize.toktok import ToktokTokenizer
from nlptools.contractions import CONTRACTION_MAP


def __load_spacy():
    return spacy.load("en_core_web_sm")


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text


def remove_accented_chars(text):
    return (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )


def remove_special_characters(text, remove_digits=False):
    special_char_pattern = re.compile(r"([{.(-)!}])")
    text = special_char_pattern.sub(" \\1 ", text)
    pattern = r"[^a-zA-z0-9\s]" if not remove_digits else r"[^a-zA-z\s]"
    text = re.sub(pattern, "", text)
    return text


def remove_stopwords(text, is_lower_case=False):
    tokenizer = ToktokTokenizer()
    stopwords = nltk.corpus.stopwords.words("english")
    stopwords.remove("no")
    stopwords.remove("not")

    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        tokens = [token for token in tokens if token not in stopwords]
    else:
        tokens = [token for token in tokens if token.lower() not in stopwords]
    return " ".join(tokens)


def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

    contractions_pattern = re.compile(
        "({})".format("|".join(contraction_mapping.keys())),
        flags=re.IGNORECASE | re.DOTALL,
    )

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = (
            contraction_mapping.get(match)
            if contraction_mapping.get(match)
            else contraction_mapping.get(match.lower())
        )
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()

    return " ".join([ps.stem(word) for word in text.split()])


def lemmatize_text(text):

    text = __load_spacy(text)
    return " ".join(
        [word.lemma_ if word.lemma_ != "-PRON-" else word.text for word in text]  # noqa: E501
    )


def remove_extra_lines(text):
    return re.sub(r"[\r|\n|\r\n]+", " ", text)


def remove_extra_whitespaces(text):
    return re.sub(" +", " ", text)


def normalize_corpus(
    corpus,
    html_stripping=True,
    contraction_expansion=True,
    accented_char_removal=True,
    text_lower_case=True,
    text_lemmatization=True,
    special_char_removal=True,
    stopword_removal=True,
    remove_digits=True,
):

    normalized_corpus = []

    for doc in corpus:
        if html_stripping:
            doc = strip_html_tags(doc)

        if accented_char_removal:
            doc = remove_accented_chars(doc)

        if contraction_expansion:
            doc = expand_contractions(doc)

        if text_lower_case:
            doc = doc.lower()

        doc = remove_extra_lines(doc)

        if text_lemmatization:
            doc = lemmatize_text(doc)

        if special_char_removal:
            doc = remove_special_characters(doc, remove_digits=remove_digits)

        doc = remove_extra_whitespaces(doc)

        if stopword_removal:
            doc = remove_stopwords(doc, is_lower_case=text_lower_case)

        normalized_corpus.append(doc)

    return normalized_corpus
