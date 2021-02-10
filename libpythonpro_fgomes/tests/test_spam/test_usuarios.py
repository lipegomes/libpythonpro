from libpythonpro_fgomes.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Filipe')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Filipe'), Usuario(nome='Luffy')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
