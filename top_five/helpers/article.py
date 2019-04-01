class Article:
    def __init__(self, _headline=None, _author=None, _url=None, _lead=None, _abstract=None, _timestamp=None, _query=None):
        self.abstract = _abstract
        self.author = _author
        self.headline = _headline
        self.lead_paragraph = _lead
        self.timestamp = _timestamp
        self.url = _url
        self.query = _query
