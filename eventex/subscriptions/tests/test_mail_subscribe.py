from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Leonardo Kiyota', cpf='12345678901',
                    email='leokiyota@gmail.com', phone='11-99595-9171')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)


    def test_subscription_email_from(self):
        #expect = 'contato@eventex.com.br'
        expect = 'leonardo.kiyota@gmail.com'

        self.assertEqual(expect, self.email.from_email)


    def test_subscription_email_to(self):
        #expect = ['contato@eventex.com.br', 'leokiyota@gmail.com']
        expect = ['leonardo.kiyota@gmail.com', 'leokiyota@gmail.com']

        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = [
                'Leonardo Kiyota',
                '12345678901',
                'leokiyota@gmail.com',
                '11-99595-9171',
            ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)