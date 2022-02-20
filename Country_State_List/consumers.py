from channels.consumer import SyncConsumer


class Country_State_ListConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass