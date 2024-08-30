from rest_framework import serializers
from .models import (
    ArnasoyTumani, BaxmalTumani, GallaorolTumani, SharofRashidovTumani, DostilikTumani,
    ZominTumani, ZarbdorTumani, MirzacholTumani, ZafarobodTumani, PaxtakorTumani,
    ForishTumani, YangiobodTumani, Jizzax
)
class ArnasoyTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArnasoyTumani
        fields = '__all__'

class BaxmalTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaxmalTumani
        fields = '__all__'

class GallaorolTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallaorolTumani
        fields = '__all__'

class SharofRashidovTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharofRashidovTumani
        fields = '__all__'

class DostilikTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = DostilikTumani
        fields = '__all__'

class ZominTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZominTumani
        fields = '__all__'

class ZarbdorTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZarbdorTumani
        fields = '__all__'

class MirzacholTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = MirzacholTumani
        fields = '__all__'

class ZafarobodTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZafarobodTumani
        fields = '__all__'
class PaxtakorTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaxtakorTumani
        fields = '__all__'

class ForishTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForishTumani
        fields = '__all__'

class YangiobodTumaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = YangiobodTumani
        fields = '__all__'

class JizzaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jizzax
        fields = '__all__'
