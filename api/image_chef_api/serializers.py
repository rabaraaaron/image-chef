from rest_framework import serializers

from api.image_chef_api.models import Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['prompt']

    prompt = serializers.CharField(
        required=True,
        allow_blank=False,
        help_text='Enter your prompt'
    )
