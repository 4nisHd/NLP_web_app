import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
text="The sky was a canvas of shifting hues, transitioning from a serene cerulean to a fiery orange as the sun descended behind the distant mountains. Birds danced in the fading light, their silhouettes weaving intricate patterns against the backdrop of the evening sky. Down below, a river meandered through the landscape, its gentle currents whispering secrets of ages past. Trees stood sentinel along the banks, their leaves rustling in the breeze like whispers from forgotten realms. Amidst this natural symphony, a lone figure sat atop a hill, lost in contemplation. Thoughts ebbed and flowed like the river below, weaving dreams of tomorrow and memories of yesterday into a tapestry of existence. As the stars began to emerge, casting their ancient light upon the world, a sense of wonder and possibility filled the air, reminding all who beheld it that in the grand tapestry of life, every thread has a story to tell."
doc = nlp(text)

tokens = [token.text for token in doc]


punctuation = punctuation + '\n'
punctuation

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1



max_frequency = max(word_frequencies.values())
max_frequency

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word] / max_frequency


sentence_tokens = [sent for sent in doc.sents]


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]



from heapq import nlargest

select_length = int(len(sentence_tokens) * 0.3)
select_length

summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
summary

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
print(summary)
