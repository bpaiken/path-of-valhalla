class SkillNode:
    def __init__(self, args):
        self._name = args['name']
        self.links = args['links']
        self._is_origin = args['is_origin']
        self.is_active = False

    def activate(self):
        if self.is_available:
            self.is_active = True

    def is_available(self):
        print("not yet implemented")
        return None