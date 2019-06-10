from django_rq import job
from api.models import Result, Search
from api.utils.searcher import Searcher

@job
def perform_search(search_id):
    search = Search.objects.get(pk=search_id)
    found_protein = Searcher().find_sequence(search.query)
    result = Result(
        search=search,
        protein=found_protein['protein'] if found_protein else None,
        location=found_protein['location'] if found_protein else -1
    )
    result.save()

    search.processed = True
    search.save()
