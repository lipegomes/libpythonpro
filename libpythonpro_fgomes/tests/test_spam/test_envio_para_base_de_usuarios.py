from unittest.mock import Mock

import pytest

from libpythonpro_fgomes.spam.main import EnviadorDeSpam
from libpythonpro_fgomes.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.eviar_emails(
        'fgdl.py91@gmail.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Filipe', email='fgdl.py91@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.eviar_emails(
        'luffy_test91@email.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
    enviador.enviar.assert_called_once_with(
        'luffy_test91@email.com',
        'fgdl.py91@gmail.com',
        'Curso Python Pro',
        'Aula arquivo Conftest.'
    )
