from rest_framework import serializers

from api.image_chef_api.models import ImageToImage, Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['prompt']

    prompt = serializers.CharField(
        required=True,
        allow_blank=False,
        help_text='Enter your prompt'
    )


class ImageToImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToImage
        fields = ['image', 'mask', 'prompt']

    image = serializers.ImageField(
        required=True
    )

    mask = serializers.ImageField(
        required=True
    )

    prompt = serializers.CharField(
        required=True,
        allow_blank=False,
        help_text='Enter your prompt'
    )
