from libpythonpro_fgomes.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Filipe', email='fgdl.py91@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Filipe', email='fgdl.py91@gmail.com'), Usuario(nome='Luffy', email='luffy_test@email.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
