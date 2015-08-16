''' general utility methods for python magic and url parsing '''
from . import camelizer


def get_methods_of_class(cls):
    ''' super hacky implementation of getting all public methods of a class '''
    return [getattr(cls, method)
            for method in dir(cls)
            if callable(getattr(cls, method)) and not method.startswith('_')]


def _get_stripped_name(name):
    ''' strips string of spaces and slashes '''
    return name.strip(' /')


def _get_urlish_name(name):
    ''' converts any name to urlish (snake case) '''
    return _get_stripped_name(camelizer.to_url_case(name))


def get_route_name(method, prefix=''):
    ''' converts a method to a urlish format.
        the prefix is class name.
        does camelCase to snake_case
        eg

        class ClassName:

            def function_name():
                pass

        returns /class_name/function_name/ '''

    return '/{0}/'.format('/'.join(
        [_get_urlish_name(prefix),
         _get_urlish_name(method.__name__)]))
