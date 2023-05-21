import os
import sys
import yaml

# print(sys.argv)
# print(sys.argv[0])
# # print(sys.argv[1])
# print(os.path.split(sys.argv[0]))
# template_dir, template_file = os.path.split(sys.argv[0])
# print(f"template_dir:  {template_dir}")
# print(template_file)
# print(os.getcwd())
# path = os.getcwd()
# template_dir = path + '/templates'
# template_file = template_dir + '.*jinja2'
# print(template_file)

# print(os.path)
# print(sys.path[0])
# print(sys.argv)

with open('yaml_data/for.yaml') as f:
    vars_dict = yaml.safe_load(f)
    print(vars_dict)

for sw in vars_dict:
    print(sw)