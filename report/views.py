from datetime import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from task.models import Task


class GetCountTask(APIView):
    """
    Generate statistics by months

    Returns data in a format:
            "labels": [
            "2022-02",
            "2022-03"
            ],
            "datasets": {
                "count_all_tasks": [
                    0,
                    2
                ],
                "count_executed_tasks": [
                    0,
                    0
                ],
                "count_expired_tasks": [
                    0,
                    2
                ]
            }

    requires the following parameters:
        start - start search date in a format: '2022-02-15 16:53'
        end - end search date in a format: '2022-02-15 16:53'

    """

    permission_classes = [permissions.IsAdminUser]

    def get(self, request):

        start = request.GET.get('start', False)
        end = request.GET.get('end', False)

        if start and end:
            start = start.rsplit('-', 1)[0]
            end = end.rsplit('-', 1)[0]

            start_date = datetime.strptime(start, "%Y-%m")
            end_date = datetime.strptime(end, "%Y-%m")

            labels = []

            count_all_tasks = []
            count_executed_tasks = []
            count_expired_tasks = []

            while start_date <= end_date:

                date_str = start_date.strftime("%Y-%m")
                labels.append(date_str)

                count_all_tasks.append(Task.objects.filter(createDateTime__gte=start_date).filter(
                    createDateTime__lte=start_date + relativedelta(months=1)).count())

                count_executed_tasks.append(Task.objects.filter(createDateTime__gte=start_date).
                                            filter(createDateTime__lte=start_date+relativedelta(months=1)).
                                            filter(is_done=True).count())

                count_expired_tasks.append(Task.objects.filter(createDateTime__gte=start_date).
                                           filter(createDateTime__lte=start_date + relativedelta(months=1)).
                                           filter(expired=True).filter(is_done=False).count())

                start_date += relativedelta(months=1)

            date_list = {
                'labels': labels,
                'datasets': {
                    'count_all_tasks': count_all_tasks,
                    'count_executed_tasks': count_executed_tasks,
                    'count_expired_tasks': count_expired_tasks,
                }
            }

            return Response(date_list)

        return Response({'parameters not specified'})