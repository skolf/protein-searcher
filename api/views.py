from rest_framework.views import APIView
from rest_framework.response import Response

class SearchList(APIView):
    def get(self, request):
        resp_dict = {
            'status': '',
            'message': '',
            'data': None
        }

        try:
            # list_ids = ListAccess.objects.values_list('list').filter(user=request.user)
            # lists = TaskList.objects.filter(id__in=list_ids).values()
            resp_dict['status'] = 'Success'
            resp_dict['message'] = 'Retrieved the list of searches'
            resp_dict['data'] = []

        except Exception as e:
            print(e)
            resp_dict['status'] = 'Failed'
            resp_dict['message'] = 'Something went wrong while fetching data. Error: '+e.__str__()
            resp_dict['data'] = None

        return Response(resp_dict)
