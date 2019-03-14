
from rest_framework import serializers

from .models import CharlaModel, CategoriaModel, UsuarioVotoModel

class UsuarioVotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioVotoModel
        fields = "__all__"


class CharlaSerializer(serializers.ModelSerializer):

    vote = UsuarioVotoSerializer(read_only=True, required=False)

    class Meta:
        model = CharlaModel
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = "__all__"
