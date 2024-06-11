# summarizer/utils.py
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

class TextSummarizer:
    def summarize(self, text, num_sentences=3):
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, sentences_count=num_sentences)
        return ' '.join([str(sentence) for sentence in summary])