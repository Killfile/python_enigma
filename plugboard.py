class Plugboard(dict):
    def __getitem__(self, key):
        if key in self:
            return super(Plugboard, self).__getitem__(key)
        else:
            return key

    def __setitem__(self, key, value):
        super(Plugboard, self).__setitem__(key, value)
        super(Plugboard, self).__setitem__(value, key)
    
    def __delitem__(self, key):
        value = self[key]
        super(Plugboard, self).__delitem__(key)
        super(Plugboard, self).__delitem__(value)