import datetime
from translation_history import TranslationHistory
import translators as ts
from collections import namedtuple


# translation_history = namedtuple("translation_history", ["src_lang", "trg_lang", "src_text", "trg_text", "date"])


class Translator:
    @staticmethod
    def translate_text(tr_history: TranslationHistory):
        tr_history.trg_text = ts.translate_text(query_text=tr_history.src_text, from_language=tr_history.src_lang,
                                                to_language=tr_history.trg_lang)
        tr_history.date = datetime.datetime.now()
        return tr_history


if __name__ == '__main__':
    history1 = TranslationHistory("hello world", "fa")
    Translator.translate_text(history1)
    print(history1.trg_text)
