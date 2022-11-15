class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)
        return self

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)
        return self

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)
        return self

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)
        return self











class LoggableList(Loggable, list):
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)








class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, a):
        if a > 0:
            super(PositiveList, self).append(a)
        else:
            raise NonPositiveError








exceptions = {}
throwed_exceptions = []

def found_path(exceptions, start, end, path=[])
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]
        if node not in path:
            newpath = found_path(exceptins, node, end, path)
            if newpath: return newpath
    return []

a = int(input())
for _ in range(a):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    exceptions[child] = parents

b = int(input())
for _ in range(b)
    throwing = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptons, throwing, throwed_exception)) > 1:
            print(throwing)
            break
    throwed_exceptions.append(throwing)