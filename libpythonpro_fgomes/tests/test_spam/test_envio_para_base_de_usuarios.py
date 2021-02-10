from libpythonpro_fgomes.spam.enviador_de_email import Enviador
from libpythonpro_fgomes.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.eviar_emails(
        'fgdl.py91@gmail.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
