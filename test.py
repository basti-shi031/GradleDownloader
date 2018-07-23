import json

# f2 = open('java500.txt', 'r')
# content = f2.read()
# print(content)
# f2.close()
#
# js = json.loads(content)
# print(type(js))
# print('test' in js.keys())
#
# f3 = open('java500.txt', 'w');
# js['test'] = 1213123
# f3.write(json.dumps(js))
# f3.close()

a = '{"a":"b"}'
content = json.loads(a)
print(content['a'])
