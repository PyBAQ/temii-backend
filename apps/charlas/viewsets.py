from rest_framework import viewsets

from .business import CharlaBusiness
from .serializers import CharlaSerializer
from .models import CharlaModel


class CharlaViewSet(viewsets.ModelViewSet):
    model = CharlaModel
    queryset = CharlaModel.objects.all()
    serializer_class = CharlaSerializer

    def get_votes(self, data_id):
        if not self.request.user.is_authenticated():
            return None
        return CharlaBusiness.get_votes_for_talks(data_id, self.request.user)

    def get_serializer(self, instance_or_qs=None, *args, **kwargs):
        data = instance_or_qs
        if self.request and self.request.method == "GET":
            if isinstance(instance_or_qs, CharlaModel):
                votes = self.get_votes(instance_or_qs.id)
                if votes:
                    instance_or_qs.vote = votes[:1][0]
                data = instance_or_qs
            else:
                instances = {instance.id: instance for instance in instance_or_qs}
                votes = self.get_votes(list(instances.keys()))
                if votes:
                    for vote in votes:
                        instances[vote.charla_id].vote = vote
                data = instances.values()
        return super().get_serializer(data, *args, **kwargs)
