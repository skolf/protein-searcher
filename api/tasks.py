from django_rq import job
from api.models import Result, Search
# from api.searcher import Searcher
from api.utils.searcher import Searcher

@job
def perform_search(search_id):
    search = Search.objects.get(pk=search_id)
    found_protein = Searcher().find_sequence(search.query)

    if found_protein is not None:
        result = Result(
            search=search,
            protein=found_protein['protein'],
            location=found_protein['location']
        )
        result.save()

    search.processed = True
    search.save()
