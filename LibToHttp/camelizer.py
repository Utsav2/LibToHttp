''' Converts snake case to camel case, and vice-versa '''
import inflection


def to_url_case(string):
    ''' Converts input to what a url should look like.
        Right now, it's snake case
        className -> class_name
        '''

    return inflection.underscore(string)
