from LibToHttp import router
from tests.base import TestCase


class SimpleClass(object):
    def __init__(self):
        pass

    def simple_method(self):
        pass

    def return_json(self):
        return {'key': 'value'}


class RouterTestCase(TestCase):

    def test_no_decoration_if_disabled(self):
        router.config.API_ROUTES_ENABLED = False
        self.assertEquals(router.route(SimpleClass)(), SimpleClass)

    def test_decoration_if_enabled(self):
        router.config.API_ROUTES_ENABLED = True
        self.assertNotEquals(router.route(SimpleClass)(), SimpleClass)

    def test_add_public_methods(self):
        router.route(SimpleClass)()
        self.assertIn('/simple_class/simple_method/', router.route_map)

    def test_not_add_private_methods(self):
        router.route(SimpleClass)()
        self.assertNotIn('/simple_class/__init__/', router.route_map)

    def test_run(self):
        # TODO The tests hang when they're run, wonder what's up
        pass

    def test_route_class_adds_flask_route(self):
        with router.app.test_request_context():
            router.Route(SimpleClass.return_json, '/test/')
            endpoints = [rule.endpoint
                         for rule in router.app.url_map.iter_rules()]
            self.assertIn('/test/', endpoints)

    def test_route_replies_200_on_success(self):
        with router.app.test_request_context():
            router.Route(SimpleClass.return_json, '/test/')
            response = router.app.view_functions['/test/']()
            self.assertEquals(response.status_code, 200)

    def test_route_replies_jsonifies_response(self):
        with router.app.test_request_context():
            router.Route(SimpleClass.return_json, '/test/')
            response = router.app.view_functions['/test/']()
            import json
            response_dict = json.loads(response.data.decode('utf-8'))
            self.assertEquals(SimpleClass().return_json(), response_dict)
