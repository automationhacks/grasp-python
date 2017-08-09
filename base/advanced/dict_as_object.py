import yaml

with open('sample.yml') as f:
    py_dict = yaml.load(f)

class Dummy:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Dummy1(object):
    def __init__(self, data):

        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Dummy1(value) if isinstance(value, dict) else value

# obj = Dummy(**py_dict['PVE-83253'])

# print(obj)

new_obj = Dummy1(py_dict['PVE-83253'])

print(new_obj.preferences.gantt_options.Milestones)
# print(obj.week_dates)

x = new_obj.preferences.gantt_options.__dict__

y = dict(new_obj.preferences.gantt_options)

print(y, type(y))