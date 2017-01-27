# <SpoofProof.net>

## Inspiration

* In the age of social media, fake news spreads like wildfire. 
* During the 2016 Presidential Election, the amount of fake news being published on the web increased significantly. 
* A new study from Stanford researchers evaluated students' ability to assess information sources and described the results as "dismaying," "bleak" and "a threat to democracy." 

This a growing problem that we wanted to address. We wish to provide a service that can help reverse this trend. 

## What it does

SproofProof is a system that tries to automatically determine whether a given source is fake. It uses several heuristics to determine if a source is fake including tone analysis (via IBM Watson) and runs the data through a trained filter to classify the source as fake or not.
 
## How we built it

SpoofProof is a django application written in python that calculates the credibility of articles on the server. First we use IBM’s Watson to calculate the tone of the given article. We then use a neural network that is given the tone data to classify the article as credible or fake. We hope to expand the system to add several layers of analysis to produce more accurate results.
 
## Challenges we ran into

One of the difficulties we ran into was the curation of a data set that we could use to train the neural network. We had to research to find both credible and fake articles that the system could learn from.
 
## What we learned

We learned a ton working on the project, especially in regards to IBM’s Watson API and Machine Learning. The Watson API proved to be a very handy resource that allowed us to get data that would otherwise require us to implement advanced natural language processing algorithms. Machine Learning is a topic that we haven’t worked with much outside of a couple small class projects. This opportunity to use Machine Learning was very beneficial to us and we learned a lot from it.
 
## What's next for SpoofProof

With such a limited amount of time we were only able to build a small training set of credible and fake news articles to train SpoofProof with. In the future, we hope to expand this training set and create a larger database of articles with their associated credibility scores. We also started implementing OCR in order to extract extra information from pictures within articles that could be analysed in a similar manner to the article body text. We also started work on analysing links to outside information in order to see how an article defends its points. We were unable to finish this task as it became clear that fake news uses lots of external links to boost search engine page rank. In the future we would like to be able to cross reference data between different sources as major events will be reported on multiple times. Another factor we believed could play a role in the credibility of an article is the overall relevance of general concepts a writer tries to address. With the power of Watson’s AlchemyLanguage, we intend to identify general concepts that aren't necessarily directly referenced in the text and use relevance scores as an additional set of input for SpoofProof’s neural net.
