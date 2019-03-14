
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