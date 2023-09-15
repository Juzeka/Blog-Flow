WAITING_APPROVED_CHOICE = 'waiting_approved'
WAITING_APPROVED_STR = 'Aguardando aprovação'
APPROVED_CHOICE = 'approved'
APPROVED_STR = 'Aprovado'
DISAPPROVED_CHOICE = 'disapproved'
DISAPPROVED_STR = 'Reprovado'


STATUS_COMMENTS_CHOICES = (
    (WAITING_APPROVED_CHOICE, WAITING_APPROVED_STR),
    (APPROVED_CHOICE, APPROVED_STR),
    (DISAPPROVED_CHOICE, DISAPPROVED_STR)
)


WAITING_PUBLICATION_CHOICE = 'waiting_publication'
WAITING_PUBLICATION_STR = 'Aguardando publicação'
PUBLISHED_CHOICE = 'published'
PUBLISHED_STR = 'Publicado'
CANCELED_CHOICE = 'canceled'
CANCELED_STR = 'Cancelado'


STATUS_ARTICLE_CHOICES = (
    (WAITING_PUBLICATION_CHOICE, WAITING_PUBLICATION_STR),
    (PUBLISHED_CHOICE, PUBLISHED_STR),
    (CANCELED_CHOICE, CANCELED_STR)
)