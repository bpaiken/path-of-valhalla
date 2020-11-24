class SkillNode:
    def __init__(self, args):
        self._name = args['name']
        self.links = args['links']
        self._is_origin = args['is_origin']
        self.is_active = False
        self.alignment = args['alignment']
        self.type = args['type']

    # Proper way to expose an instance variable
    # def type(self, t = None):
    #     if t: self._type = t
    #     try: return self._type
    #     except AttributeError: return None

    def activate(self):
        if self.is_available:
            self.is_active = True
            return True
        else:
            return False

    def is_available(self):
        print("not yet implemented")
        return None