from rest_framework import serializers

from .models import ClientRequestModel, AnswerModel


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerModel
        fields = ['id', 'client_request', 'support_text', 'published']


class ClientRequestSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    # answers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ClientRequestModel
        fields = ['id', 'status',  'name', 'request_client', 'published', 'answers']
        depth = 2

    def create(self, validated_data):
        print(validated_data)
        validated_data.pop('answers')
        instance = ClientRequestModel(**validated_data)
        instance.save()
        instance.answers.set([])
        return instance

    def update(self, instance, validated_data):
        stat = validated_data.pop('status')
        instance.status = stat
        instance.save()
        return instance
