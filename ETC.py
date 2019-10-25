'''
    A text search module that clusters and returns query-relevant documents along with a cluster category
        Example Usage:
            etc = ETC(documents)
            etc.fit()
            description, cluster = etc.find("Is there water on Mars?")
'''
import spacy
class ETC():

    '''
        Create a new Explainable Text Cluster object
            @docs - a list of plain text documents
    '''
    def __init__(self, docs):
        if not docs:
            raise Exception("Invalid Argument: docs cannot be empty")
        self.docs = docs
        self._fitted = False
        #TODO(Mike): other initialization logic

    '''
        Clean, encode, and cluster a document set
            @cutoff_margin - where to cutoff common words
    '''
    def fit(self, cutoff_margin):
        cleaned = self._clean(cutoff_margin)
        encoded = self._encode(cleaned)
        self.clusters = self._cluster(encoded)

        self._fitted = True

    '''
        Splits a document into words, lemmatizes and then culls common words
            @cutoff_margin - where to cutoff common words
    '''
    def _clean(self, cutoff_margin, corpus):
        #TODO(Mike): split and lemmatize documents
        
        nlp = spacy.load('en_core_web_sm')
        docs = [nlp(article) for article in corpus]
        
        # create tokens
        token_doc = [''] * len(docs)
        for i in range(len(docs)):
            token_doc[i] = [token.text  for token in docs[i]]
            
        # lemmetization
        lemmas = [''] * len(docs)
        for i in range(len(token_doc)):
            lemmas[i] = [token.lemma_ for token in docs[i]]
            
            
        #TODO(Mike): remove common words ('a', 'and', 'the', etc.)
        # in-built stop words in spacy    
        stop_words = spacy.lang.en.stop_words.STOP_WORDS
        no_stop_lemmas =[''] * len(docs)
        for i in range(len(docs)):
            no_stop_lemmas[i] = [lemma for lemma in lemmas if lemma.isalpha() and lemma not in stop_words]


        pass

    '''
        Turns a document list (a vector of vectors of words) into a vector of matrices
            @documents - a list of tokenized, lemmatized lists of words
    '''
    def _encode(self, documents):
        #TODO(Mike): implement preferred encoding method
        pass

    '''
        Turns a document list (a vector of matrices) into clusters (a vector of vectors of matrices)
            @encodings - a list of encoded documents
    '''
    def _cluster(self, encodings):
        #TODO(Mike): implement preferred clustering method
        pass

    '''
        Predicts the cluster assignment of a query against the fitted document set
            @doc - a plain text document
    '''
    def _predictCluster(self, query):
        cleaned = self._clean([query])
        encoded = self._encode(cleaned)
        #TODO(Mike): implement preferred cluster prediction method

    '''
        Turns a cluster (a vector of matrices) into natural language phrases
            @cluster - a list of document vectors
    '''
    def _describeCluster(self, cluster):
        #TODO(Mike): generate a cluster description
        pass

    '''
        Search a fitted document set and retrieve the relevant documents and their description
            @query - a plain text string
    '''
    def find(self, query):
        if not self._fitted:
            self.fit(cutoff_margin=50)

        cluster = self._predictCluster(query)
        description = self._describeCluster(cluster)

        return description, cluster
