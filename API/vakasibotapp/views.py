from rest_framework import generics
from .models import (
    ArnasoyTumani, BaxmalTumani, GallaorolTumani, SharofRashidovTumani, DostilikTumani,
    ZominTumani, ZarbdorTumani, MirzacholTumani, ZafarobodTumani, PaxtakorTumani,
    ForishTumani, YangiobodTumani, Jizzax
)
from .serializers import (
    ArnasoyTumaniSerializer, BaxmalTumaniSerializer, GallaorolTumaniSerializer,
    SharofRashidovTumaniSerializer, DostilikTumaniSerializer, ZominTumaniSerializer,
    ZarbdorTumaniSerializer, MirzacholTumaniSerializer, ZafarobodTumaniSerializer,
    PaxtakorTumaniSerializer, ForishTumaniSerializer, YangiobodTumaniSerializer, JizzaxSerializer
)

class ArnasoyTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = ArnasoyTumani.objects.all()
    serializer_class = ArnasoyTumaniSerializer

class ArnasoyTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArnasoyTumani.objects.all()
    serializer_class = ArnasoyTumaniSerializer

class BaxmalTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = BaxmalTumani.objects.all()
    serializer_class = BaxmalTumaniSerializer

class BaxmalTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaxmalTumani.objects.all()
    serializer_class = BaxmalTumaniSerializer

class GallaorolTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = GallaorolTumani.objects.all()
    serializer_class = GallaorolTumaniSerializer

class GallaorolTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GallaorolTumani.objects.all()
    serializer_class = GallaorolTumaniSerializer

class SharofRashidovTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = SharofRashidovTumani.objects.all()
    serializer_class = SharofRashidovTumaniSerializer

class SharofRashidovTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SharofRashidovTumani.objects.all()
    serializer_class = SharofRashidovTumaniSerializer

class DostilikTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = DostilikTumani.objects.all()
    serializer_class = DostilikTumaniSerializer

class DostilikTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DostilikTumani.objects.all()
    serializer_class = DostilikTumaniSerializer

class ZominTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = ZominTumani.objects.all()
    serializer_class = ZominTumaniSerializer

class ZominTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZominTumani.objects.all()
    serializer_class = ZominTumaniSerializer

class ZarbdorTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = ZarbdorTumani.objects.all()
    serializer_class = ZarbdorTumaniSerializer

class ZarbdorTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZarbdorTumani.objects.all()
    serializer_class = ZarbdorTumaniSerializer

class MirzacholTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = MirzacholTumani.objects.all()
    serializer_class = MirzacholTumaniSerializer

class MirzacholTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MirzacholTumani.objects.all()
    serializer_class = MirzacholTumaniSerializer

class ZafarobodTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = ZafarobodTumani.objects.all()
    serializer_class = ZafarobodTumaniSerializer

class ZafarobodTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZafarobodTumani.objects.all()
    serializer_class = ZafarobodTumaniSerializer

class PaxtakorTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaxtakorTumani.objects.all()
    serializer_class = PaxtakorTumaniSerializer

class PaxtakorTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaxtakorTumani.objects.all()
    serializer_class = PaxtakorTumaniSerializer

class ForishTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = ForishTumani.objects.all()
    serializer_class = ForishTumaniSerializer

class ForishTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForishTumani.objects.all()
    serializer_class = ForishTumaniSerializer

class YangiobodTumaniListCreateAPIView(generics.ListCreateAPIView):
    queryset = YangiobodTumani.objects.all()
    serializer_class = YangiobodTumaniSerializer

class YangiobodTumaniRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YangiobodTumani.objects.all()
    serializer_class = YangiobodTumaniSerializer

class JizzaxListCreateAPIView(generics.ListCreateAPIView):
    queryset = Jizzax.objects.all()
    serializer_class = JizzaxSerializer

class JizzaxRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jizzax.objects.all()
    serializer_class = JizzaxSerializer
