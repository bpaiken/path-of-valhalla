from skill_node import SkillNode, StatSkillNode
from types import SkillNodeType

class SkillTree:
    def __init__(self, json_input = None):
        if json_input: self._input = json_input
        if json_input['clusters']: self._clusters = json_input['clusters']
        self._node_tree = self.build_node_tree(self._clusters)

    def activate_node(self, node_id):
        node = self._node_tree['node_id']
        if node and self.can_be_activated(node):
            node.activate()
            return node
        else:
            print("node {} is not available".format(node_id))
            return node
    
    def deactivate_node(self, node_id):
        node = self._node_tree['node_id']
        # todo: node not found

        if node.is_active() == False:
            return node

        if self.can_be_deactivated(node):
           node.deactivate()
        else:
            print("node {} cannot be deactivated".format(node_id))
        return node

    def can_be_activated(self, node):
        for linked_node in node.links:
            return True if linked_node.is_active() else False

    def can_be_deactivated(self, node):
        return self.can_be_deactivated_loop(node, node.id())
    
    def can_be_deactivated_loop(self, node, calling_node_id):
        linked_node_ids = node.links()
        linked_node_ids.remove(calling_node_id)
        linked_nodes = self.get_node_list(linked_node_ids, True) # list of ACTIVE linked nodes
        if(len(linked_nodes == 0)): 
            return False

        result = True
        node_id = node.id()
        for linked_node in linked_nodes:
            if(self.is_origin(linked_node)): 
                break # stop the recursive chain if node is origin
            result = self.can_be_deactivated_loop(linked_node, node_id)
        
        return result
        
    def is_origin(self, node):
        return True if node.type() == SkillNodeType.origin() else False

    def get_node_list(self, node_ids, active_only = False):
        node_list = []
        for node_id in node_ids:
            node = self._node_tree[node_id]
            if((active_only == False) or (active_only and node.is_active)):
                node_list.append(node)
        return node_list

    def build_node_tree(self, clusters):
        # want node tree to take the form of dictionary w/ { nodeId: node }
        # this will allow us to quickly/easily access nodes as needed, without having to search through an array
        node_tree = {}
        for cluster in clusters:
            if 'skill_nodes' in cluster: skill_nodes = cluster['skill_nodes']
            for node_object in skill_nodes:
                node = self.build_skill_node(node_object)
                if node:
                    node_tree[node.id] = node
                # end node loop
            # end cluster loop
        return node_tree

    def build_skill_node(self, node_object):
        node_type = node_object['type']
        if node_type == SkillNodeType.stat():
            return StatSkillNode(node_object)

        elif node_type == SkillNodeType.gear():
            # todo
            pass

        elif node_type == SkillNodeType.notable():
            # todo
            pass

        elif node_type == SkillNodeType.origin():
            # todo
            pass
        
        else: 
            return None
