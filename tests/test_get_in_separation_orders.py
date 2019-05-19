from lojaintegrada import Api


def test_get_in_separation_orders(mocker):
    mock_get_orders = mocker.patch.object(Api, 'get_orders')

    api = Api(api_key='fake-api-key', app_key='fake-app-key')
    res = api.get_in_separation_orders()

    mock_get_orders.assert_called_with(
        limit=50,
        situacao_id=15
    )

    assert res == mock_get_orders.return_value


def test_get_in_separation_orders_with_custom_limit(mocker):
    mock_get_orders = mocker.patch.object(Api, 'get_orders')

    api = Api(api_key='fake-api-key', app_key='fake-app-key')
    res = api.get_in_separation_orders(limit=20)

    mock_get_orders.assert_called_with(
        limit=20,
        situacao_id=15
    )

    assert res == mock_get_orders.return_value


def test_get_in_separation_orders_with_custom_filters(mocker):
    mock_get_orders = mocker.patch.object(Api, 'get_orders')

    api = Api(api_key='fake-api-key', app_key='fake-app-key')
    res = api.get_in_separation_orders(cliente_id=12345)

    mock_get_orders.assert_called_with(
        limit=50,
        situacao_id=15,
        cliente_id=12345
    )

    assert res == mock_get_orders.return_value
