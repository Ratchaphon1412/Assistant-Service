from djoser.serializers import UserCreateSerializer


class AssistantsUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'password',
                  'first_name', 'last_name', 'username')
