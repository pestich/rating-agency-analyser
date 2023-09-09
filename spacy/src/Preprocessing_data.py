import spacy
from typing import List
import re

class Preprocessing_data:

    @classmethod
    def drop_tail(cls, text):
        if 'агентство НКР' in text:
            return text.split('Регуляторное раскрытие')[0]
        elif 'Национальное Рейтинговое Агентство' in text:
            text = text.split('(далее – НРА, Агентство)')[1]
            return text.split('ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ')[0]
        elif 'АКРА' in text:
            return text.split('Регуляторное раскрытие')[0]
        elif 'Эксперт РА' in text:
            return text.split('Контакты для СМИ')[0]
        return text


    @classmethod
    def clear(cls, text: str) -> str:
        nlp = spacy.load('ru_core_news_lg')
        ner_list = ['ORG', 'LOC']
        result = []
        doc = nlp(text)
        for token in doc:
            if token.ent_type_ not in ner_list and token.is_stop != True and token.is_punct != True:
                result.append(token.text.lower())
        text =  ' '.join(result)
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
        text = re.sub(r'[^а-яА-Я ]', '', text)
        text = text.replace('\n', ' ')
        text = text.replace('.', '. ')
        text = text.replace(',', ', ')
        text = re.sub('\s+', ' ', text)
        return text.strip()
    

    @classmethod
    def lemmatize(cls, text):
        nlp = spacy.load('ru_core_news_lg')
        result = []
        doc = nlp(text)
        for token in doc:
            result.append(token.lemma_)
        return ' '.join(result)\


    # @classmethod   
    # def tokenize_it(cls, text: str) -> List:
    #     nlp = spacy.load('ru_core_news_lg')
    #     nlp.Defaults.stop_words.update({'год', 'уровень', 'агентство', 'руб', 'млрд', 'компания', 'рейтинг'})
    #     result = []
    #     doc = nlp(text)
    #     for token in doc:
    #         if token.is_stop != True and token.is_punct != True:
    #             result.append(token.text)
    #     return ' '.join(result)
    

