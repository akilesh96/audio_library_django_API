from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collection.serializers import SongDetailsSerializer, AudiobookDetailsSerializer, \
    PodcastDetailsSerializer, SongDetails, PodcastDetails, AudiobookDetails

class Content(APIView):
    def get(self, request, audiotype, pk=None):
        try:
            if not pk:
                if audiotype == "song":
                    songs = SongDetails.objects.all()
                    serializer = SongDetailsSerializer(songs, many=True)
                    return Response(serializer.data)
                elif audiotype == "podcast":
                    podcasts = PodcastDetails.objects.all()
                    serializer = PodcastDetailsSerializer(podcasts, many=True)
                    return Response(serializer.data)
                elif audiotype == "audiobook":
                    audiobooks = AudiobookDetails.objects.all()
                    serializer = AudiobookDetailsSerializer(audiobooks, many=True)
                    return Response(serializer.data)

            else:
                obj, serializer_class = self.get_content_details(audiotype, pk)
                serializer_obj = serializer_class(obj)
                return Response(serializer_obj.data)


        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, audiotype, pk):
        try:
            obj, serializer_class = self.get_content_details(audiotype, pk)
            serializer_obj = serializer_class(obj, data=request.data)

            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

    def delete(self, request, audiotype, pk):
        try:
            obj, _ = self.get_content_details(audiotype, pk)
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_400_BAD_REQUEST)       

    def get_content_details(self, audiotype, pk):
        if audiotype == "song":
            obj = SongDetails.objects.get(pk=pk)
            serializer_class = SongDetailsSerializer
        elif audiotype == "podcast":
            obj = PodcastDetails.objects.get(pk=pk)
            serializer_class = PodcastDetailsSerializer
        elif audiotype == "audiobook":
            obj = AudiobookDetails.objects.get(pk=pk)
            serializer_class = AudiobookDetailsSerializer
        return obj, serializer_class


class AddContent(APIView):
    def post(self, request, audiotype):
        try:
            if audiotype == "song":
                serializer_obj = SongDetailsSerializer(data=request.data)
            elif audiotype == "podcast":
                serializer_obj = PodcastDetailsSerializer(data=request.data)
            elif audiotype == "audiobook":
                serializer_obj = AudiobookDetailsSerializer(data=request.data)

            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=status.HTTP_200_OK)

            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)