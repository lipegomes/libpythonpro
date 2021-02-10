from libpythonpro_fgomes.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def teste_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'fgdl.py91@gmail.com',
        'filipegomesdev@gmail.com',
        'Curso Python Pro',
        'Aula sobre TDD e Baby Steps.'
    )
    assert 'fgdl.py91@gmail.com' in resultado