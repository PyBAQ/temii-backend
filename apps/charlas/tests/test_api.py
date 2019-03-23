import json

from test_plus import APITestCase

from django.contrib.auth.models import User

from ..models import CategoriaModel, CharlaModel

from ..factories import UserFactory, CategoriaFactory, CharlaFactory

class TestApiCharla(APITestCase):

    @classmethod
    def setUpTestData(cls):
        UserFactory()
        CategoriaFactory()

    def setUp(self):
        self.user = User.objects.get()
        self.categoria = CategoriaModel.objects.get()

    def test_get_charla(self):
        self.get("/api/talks/")
        self.response_200()

    def test_post_charla(self):
        with self.login(self.user):
            self.post("/api/talks/", data={
                "titulo": "Titulo",
                "estado": CharlaModel.ESTADO_POSIBLE,
                "usuario": self.user.id,
                "categorias": [self.categoria.id]
            })
            self.response_201()
        self.assertEqual(1, CharlaModel.objects.all().count())

    def test_delete_charla(self):
        charla = CharlaFactory()
        with self.login(self.user):
            self.delete("/api/talks/{}/".format(charla.id))
            self.response_204()
        self.assertEqual(0, CharlaModel.objects.all().count())

    def test_patch_charla(self):
        charla = CharlaFactory()
        with self.login(self.user):
            self.patch("/api/talks/{}/".format(charla.id), data={
                "titulo": "new titulo",
            })
            self.response_200()
        self.assertEqual(1, CharlaModel.objects.all().count())
        charla.refresh_from_db()
        self.assertEqual(charla.titulo, "new titulo")

    def test_get_only_posibles_charlas(self):
        charla = CharlaFactory()
        charla = CharlaFactory(estado=CharlaModel.ESTADO_AGENDADO)
        charla = CharlaFactory(estado=CharlaModel.ESTAOO_FINALIZADO)
        self.get("/api/talks/?estado={}".format(CharlaModel.ESTADO_POSIBLE))
        self.response_200()
        content = json.loads(self.last_response.content.decode("utf-8"))
        self.assertEqual(len(content), CharlaModel.objects.filter(estado=CharlaModel.ESTADO_POSIBLE).count())
