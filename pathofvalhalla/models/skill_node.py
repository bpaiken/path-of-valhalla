class SkillNode:
    def __init__(self, args):
        # self._name = args['name']
        self._id = args['id']
        self._links = args['links']
        self._is_active = False
        # self.alignment = args['alignment'] #do we need this?
        self._type = args['type']

    # Proper way to expose an instance variable w/ setter
    # def type(self, t = None):
    #     if t: self._type = t
    #     try: return self._type
    #     except AttributeError: return None
    
    def type(self):
        return self._type

    def is_active(self):
        return self._is_active

    def activate(self):
        self._is_active = True
    
    def deactivate(self):
        self._is_active = False

    def links(self):
        return self._links

    def id(self):
        return self._id

class StatSkillNode(SkillNode):
    def __init__(self, args):
        self.value = args['value']
        self.stat = args['stat']
        super().__init__(args)