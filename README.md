# Trump-Speech-NLP
Analyzing Trump Speech Transcripts Using NLP and determine topics. Recommend to the DNC talking points to gain support from opposition in order to unify the nation.

## Data
Donald Trump October 2020 Speech Transcripts [here](https://www.rev.com/blog/transcripts/donald-trump-rally-speech-transcript-goodyear-az-october-28)

## Skills & Tools
1. Topic Modeling - NMF and Scikit-learn
2. Preprocessing - spaCy
3. Visualizations - Plotly
4. Web-scraping - BeautifulSoup

## Depdendencies
1. web_scrape.py
  - The get_transcript function uses BeautifulSoup to reteive transcript texts and stores it
2. preprocess.py
  - The clean and preprocess functions tokenize, removes stop words/punctuations, and lemmatizes corpus
