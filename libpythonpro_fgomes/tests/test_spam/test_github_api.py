from unittest.mock import Mock

from libpythonpro_fgomes import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'lipegomes',
        'id': 61765381,
        'node_id': 'MDQ6VXNlcjYxNzY1Mzgx',
        'avatar_url': 'https://avatars.githubusercontent.com/u/61765381?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('lipegomes')
    assert 'https://avatars.githubusercontent.com/u/61765381?v=4' == url
