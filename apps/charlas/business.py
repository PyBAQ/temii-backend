from django.db.models import F

from .models import UsuarioVotoModel

class CharlaBusiness:

    @classmethod
    def get_votes_for_talks(cls, talks_ids, user_id):
        votes = UsuarioVotoModel.objects.filter(usuario_id=user_id)
        if isinstance(talks_ids, list):
            votes = votes.filter(charla_id__in=talks_ids)
        else:
            votes = votes.filter(charla_id=talks_ids)
        if not votes.exists():
            return None
        return votes

    @classmethod
    def vote(cls, talk, user):
        votes = UsuarioVotoModel.objects.filter(usuario=user, charla=talk)
        if votes.exists():
            vote = votes[:1][0]
            vote = not vote.active
        else:
            vote = UsuarioVotoModel(usuario=user, charla=talk)
        vote.save()
        num_vote = 1 if vote.active else -1
        talk.votos = F("votos") + num_vote
        talk.save()
        return vote
