import os
from django.http import FileResponse

from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from api.image_chef_api.serializers import ImageInpaintingSerializer, ImageToImageSerializer, PromptSerializer
from api.image_chef_api.services.generate_image_to_image import generate_image_to_image
from api.image_chef_api.services.generate_text_to_image import generate_text_to_image
from api.image_chef_api.services.generate_image_inpainting import generate_text_guided_image_inpainting


@api_view(['GET'])
def health(request):
    return Response({'message': 'Hello, world!'})


SERIALIZATION_ERROR = 'Serialization error'
SERIALIZATION_ERROR_STATUS = 422


@api_view(['POST'])
@renderer_classes([StaticHTMLRenderer])
def text_to_image(request):
    serializer = PromptSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'message': SERIALIZATION_ERROR},
            status=SERIALIZATION_ERROR_STATUS
        )
    prompt = request.data.get('prompt')
    generate_text_to_image(prompt=prompt)
    file_path = './flux-schnell.png'
    if os.path.exists(file_path):
        image = open(file_path, 'rb')
        response = FileResponse(
            image,
            as_attachment=True,
            filename='generated_image.png'
        )
        return response


@api_view(['POST'])
def text_guided_image_to_image(request):
    parser_classes = [MultiPartParser, FormParser]
    serializer = ImageToImageSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'message': SERIALIZATION_ERROR},
            status=SERIALIZATION_ERROR_STATUS
        )
    image = request.FILES.get('image')
    prompt = request.data.get('prompt')

    print(f'IMAGE: {image.name}')
    print(f'PROMPT: {prompt}')

    generate_image_to_image(image=image, prompt=prompt)
    file_path = "flux-refinement.png"
    if os.path.exists(file_path):
        image = open(file_path, 'rb')
        response = FileResponse(
            image,
            as_attachment=True,
            filename='generated_image.png'
        )
        return response


@api_view(['POST'])
def image_inpainting(request):
    parser_classes = [MultiPartParser, FormParser]
    serializer = ImageInpaintingSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'message': SERIALIZATION_ERROR},
            status=SERIALIZATION_ERROR_STATUS
        )
    image = request.FILES.get('image')
    mask = request.FILES.get('mask')
    prompt = request.data.get('prompt')

    print(f'IMAGE: {image.name}')
    print(f'MASK: {mask.name}')
    print(f'PROMPT: {prompt}')

    generate_text_guided_image_inpainting(
        image=image, mask=mask, prompt=prompt)
    file_path = "flux-fill-dev.png"
    if os.path.exists(file_path):
        image = open(file_path, 'rb')
        response = FileResponse(
            image,
            as_attachment=True,
            filename='generated_image.png'
        )
        return response


@api_view(['POST'])
def improve_image_quality(request):
    serializer = PromptSerializer(data=request.data)
    if serializer.is_valid():
        print(f'PROMPT: {request.data.get("prompt")}')
        return Response({'message': 'Received request to improve image quality'})
    return Response(
        {'message': SERIALIZATION_ERROR},
        status=SERIALIZATION_ERROR_STATUS
    )
