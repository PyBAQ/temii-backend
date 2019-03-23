import factory
from factory import fuzzy
from django.contrib.auth.models import User

from .models import CharlaModel, CategoriaModel


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%s' % n)

    class Meta:
        model = User

    @factory.post_generation
    def check_password(obj, create, extracted, **kwargs):
        if obj.pk and len(obj.password) == 0:
            obj.set_password("password")
            obj.save()


class CharlaFactory(factory.django.DjangoModelFactory):
    estado = CharlaModel.ESTADO_POSIBLE
    titulo = fuzzy.FuzzyText()
    usuario = factory.SubFactory(UserFactory)

    class Meta:
        model = CharlaModel


class CategoriaFactory(factory.django.DjangoModelFactory):
    nombre = fuzzy.FuzzyText()

    class Meta:
        model = CategoriaModel
