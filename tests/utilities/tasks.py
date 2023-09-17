from django.test import TestCase
from utilities.tasks import notify_email


class UtilitiesTasksTestCase(TestCase):
    def test_notify_email(self):
        params = {
            'subject': 'Assunto',
            'message': 'Mensagem',
            'from_email': 'testing@blogflow.com',
            'recipient_list': ['fulano@hotmail.com']
        }
        result = notify_email(kwargs=params)

        self.assertEqual(result['detail'], 'E-mail enviado com sucesso.')
