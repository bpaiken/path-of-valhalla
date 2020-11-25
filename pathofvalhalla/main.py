import json
from models.types import SkillNodeType
from models.skill_node import StatSkillNode

def main():
    print("hello valhalla")

date = None
with open("../data/skill_tree.json", "r") as read_file:
    data = json.load(read_file)

print(type(data))

skill_dictionary = {}
skill_nodes = data['clusters'][1]['skill_nodes']
for node in skill_nodes:
    if(node['type'] == SkillNodeType.stat()):
        snode = StatSkillNode(node)
        skill_dictionary[node['id']] = snode
    pass

print(skill_dictionary['stomp|1'].links)

if __name__ == '__main__' : main()