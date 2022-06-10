from app.utils import get_item
from app.parameters import selectors
class Opinion:
    def __init__(self, author="",recomendation=None,stars=0
    , content="",useful=0,useless=0,publish_date=None,purchase_date=None,
    pros=[], cons=[],opinion_id=""):
        self.author = author
        self.recomendation = recomendation
        self.stars = stars
        self.content = content
        self.useful = useful
        self.useless = useless
        self.publish_date = publish_date
        self.purchase_date = purchase_date
        self.pros = pros
        self.cons = cons
        self.opinion_id = opinion_id
        return self

    def extract_opinion(self,opinion):
        for key, value in selectors.items():
            setattr(self,key,get_item(opinion, *value))
        self.opinion_id = opinion
        ["data-entry-id"]
        return self