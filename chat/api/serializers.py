from rest_framework import serializers

from chat.models import Chat, Contact
from chat.views import get_user_contact
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants','memebers_name')
        # read_only = ('id')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        curr_user = self.context['request'].user
        if (len(Contact.objects.filter(user=curr_user)) == 0):
            Contact.objects.create(user=curr_user)
        usernames=''   
        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
            usernames += username.capitalize() + '_'
        usernames=usernames[:-1]
        chat.memebers_name=usernames
        chat.save()
        return chat



# do in python shell to see how to serialize data

# from chat.models import Chat
# from chat.api.serializers import ChatSerializer
# chat = Chat.objects.get(id=1)
# s = ChatSerializer(instance=chat)
# s
# s.data
