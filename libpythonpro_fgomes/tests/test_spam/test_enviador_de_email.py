import pytest

from libpythonpro_fgomes.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['test@email.com', 'fgdl.py91@gmail.com']
)
def teste_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'filipegomesdev@gmail.com',
        'Curso Python Pro',
        'Aula sobre TDD e Baby Steps.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'fgdl']
)
def teste_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'filipegomesdev@gmail.com',
            'Curso Python Pro',
            'Aula sobre TDD e Baby Steps.'
        )
