class SlideList (list) :
    def __init__ (self, keys : list, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.keys = keys

    def __sub__ (self, val) :
        self.pop(self.keys.index(val))
        self.keys.remove(val)
        return self

    def no (self, val) :
        return self - val


