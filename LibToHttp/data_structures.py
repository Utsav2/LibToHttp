''' Simple Data Structures '''


class NoDuplicateDict(dict):
    '''Doesn't allow setting to a key if there's a value for it already '''

    # http://stackoverflow.com/a/4999321/3399432
    def __setitem__(self, key, value):
        if key in self.keys():
            raise ValueError('{0} already has a value {1}, so cannot set {2}'
                             .format(key, self[key], value))
        else:
            return super(NoDuplicateDict, self).__setitem__(key, value)
