class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,category,language):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.language = language

class Article:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author,title,description,url,image,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
