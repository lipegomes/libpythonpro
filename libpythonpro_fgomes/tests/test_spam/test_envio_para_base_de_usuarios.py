import pytest

from libpythonpro_fgomes.spam.enviador_de_email import Enviador
from libpythonpro_fgomes.spam.main import EnviadorDeSpam
from libpythonpro_fgomes.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Filipe', email='fgdl.py91@gmail.com'),
            Usuario(nome='Luffy', email='luffy_test@email.com')
        ],
        [
            Usuario(nome='Filipe', email='fgdl.py91@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.eviar_emails(
        'fgdl.py91@gmail.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Filipe', email='fgdl.py91@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.eviar_emails(
        'luffy_test91@email.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
    assert enviador.parametros_de_envio == (
        'luffy_test91@email.com',
        'fgdl.py91@gmail.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
