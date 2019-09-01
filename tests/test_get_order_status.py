from lojaintegrada import Api


def test_get_order_status(mocker):
    mock_make_request = mocker.patch.object(Api, '_make_request')

    api = Api(api_key='fake-api-key', app_key='fake-app-key')
    order = api.get_order_status(12345)

    mock_make_request.assert_called_with(
        'GET', 'https://api.awsli.com.br/api/v1/situacao/pedido/12345'
    )

    assert order == mock_make_request.return_value
