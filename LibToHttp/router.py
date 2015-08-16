''' Router '''

from flask import Flask, jsonify
from . import config
from .data_structures import NoDuplicateDict
from .utils import get_methods_of_class, get_route_name

# pylint: disable=C0103
route_map = NoDuplicateDict()
app = Flask(__name__)


class Route(object):
    ''' Defines an API route. '''

    def _get_json_wrapped_function(self, func):
        ''' wraps a method's response with http headers etc.
            right now, assumes it'll all be json. '''

        def _jsonify_wrapper(*args, **kwargs):
            ''' internal wrapper that calls the given library function '''
            return jsonify(func(self, *args, **kwargs))

        return _jsonify_wrapper

    def __init__(self, method, route_name):
        app.add_url_rule(route_name, route_name,
                         view_func=self._get_json_wrapped_function(method))


def _create_route(method, route_name=None, prefix='/'):
    ''' creates a route from a method '''
    if not route_name:
        route_name = get_route_name(method, prefix)
    route_map[route_name] = Route(method, route_name)


def _create_route_from_class(cls):
    ''' creates a route from a class definition '''
    for method in get_methods_of_class(cls):
        _create_route(method, prefix=cls.__name__)


def route(cls):
    ''' decorator for classes '''

    def router():
        ''' adds a route to the given class, internal '''
        if not config.API_ROUTES_ENABLED:
            return cls
        else:
            _create_route_from_class(cls)

    return router


def run():
    ''' starts the server. raises a value error if api routes were disabled '''

    if not config.API_ROUTES_ENABLED:
        raise ValueError('LibToHttp: called run on a disabled app')

    app.run(debug=True)


def reset():
    ''' resets the state of the module '''
    # pylint: disable=W0603
    global route_map
    global app
    route_map = NoDuplicateDict()
    app = Flask(__name__)
