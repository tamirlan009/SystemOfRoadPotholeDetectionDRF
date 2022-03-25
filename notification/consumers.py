from django.contrib.auth.models import Group
from channels.db import database_sync_to_async
from rest_framework import status
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverConsumerMixin, action
from djangochannelsrestframework.observer import model_observer
from .models import TaskNotificationTable, DetectionNotificationTable
from .serializers import TaskNotificationSerializer, DetectionNotificationSerializer


class NotificationConsumer(ObserverConsumerMixin, GenericAsyncAPIConsumer):
    queryset = TaskNotificationTable.objects.all()
    serializer_class = TaskNotificationSerializer

    """
    Subscribe to TaskNotification table
    """

    @action()
    async def subscribe_task_notification_activity(self, request_id, **kwargs):
        await self.task_notification_activity.subscribe(request_id=request_id, user=self.scope['user'])

    @model_observer(TaskNotificationTable, filter='hi')
    async def task_notification_activity(self, message, action, subscribing_request_ids=[], **kwargs):
        for request_id in subscribing_request_ids:
            group: Group = await self.get_group(message['group_id'])

            if group is not None:
                if self.scope['user'].is_creator and message['type'] == 'answer':
                    await self.reply(data=[message], action=action, request_id=request_id)
                if self.scope['user'].is_executor and message['type'] == 'new task':
                    await self.reply(data=[message], action=action, request_id=request_id)
                else:
                    await self.reply(data=[], action=action, request_id=request_id)

    @task_notification_activity.serializer
    def task_notification_activity_serializer(self, instance: TaskNotificationTable, action, **kwargs):
        # group: Group = self.get_group(1)
        # print(self.scope['user'])
        # print(instance.task_id.executor)
        return TaskNotificationSerializer(instance).data

    @task_notification_activity.groups_for_consumer
    def classroom_change_handler(self, user=None,  **kwargs):
        print(user)
        # This is called when you subscribe/unsubscribe
        if user is not None:
            yield f'-school__{user.pk}'




    """"""

    """
    Subscribe to DetectionNotificationTable
    """

    @action()
    async def subscribe_detection_notification_activity(self, request_id, **kwargs):
        await self.detection_notification_activity.subscribe(request_id=request_id)

    @model_observer(DetectionNotificationTable, serializer_class=DetectionNotificationSerializer)
    async def detection_notification_activity(self, message, action, subscribing_request_ids=[], **kwargs):
        for request_id in subscribing_request_ids:
            if self.scope['user'].id == message['recipient']:
                await self.reply(data=[message], action=action, request_id=request_id)
            else:
                await self.reply(data=[], action=action, request_id=request_id)

    """"""

    """
    Get TaskNotification list
    """

    @action()
    def get_task_notification_list(self, **kwargs):
        groups = self.scope['user'].groups.all()

        if self.scope['user'].is_creator:
            queryset = TaskNotificationTable.objects.filter(group_id__in=groups).filter(type='answer').\
                filter(task_id__creator=self.scope['user']).all()

        elif self.scope['user'].is_executor:
            queryset = TaskNotificationTable.objects.filter(group_id__in=groups).filter(type='new task').\
                filter(task_id__executor=self.scope['user']).all()
        else:
            return [], status.HTTP_200_OK

        serializer = TaskNotificationSerializer(queryset, many=True)

        return serializer.data, status.HTTP_200_OK

    """"""

    """
    Get DetectionNotification list
    """

    @action()
    def get_detection_notification_list(self, **kwargs):

        if self.scope['user'].is_creator:
            queryset = DetectionNotificationTable.objects.filter(recipient=self.scope['user']).all()
        else:
            return [], status.HTTP_200_OK

        serializer = DetectionNotificationSerializer(queryset, many=True)

        return serializer.data, status.HTTP_200_OK

    """"""

    @database_sync_to_async
    def get_group(self, group_id) -> Group:
        return self.scope['user'].groups.filter(id=group_id).first()



