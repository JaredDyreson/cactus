from rply.token import BaseBox

info_map = {
  "cpsc-120": "Introduction to C++"
}

class Target(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("Target: {}".format(self.value))
        return self.value

class Op(BaseBox):
    def __init__(self, target):
        self.target = target

class Install(Op):
    def eval(self):
      print("[+] Installing {}".format(self.target))

class Remove(Op):
    def eval(self):
      print("[+] Removing {}".format(self.target))

class Describe(Op):
    def eval(self):
      try:
          print("[+] Information about {}".format(self.target))
          print(info_map[self.target.lower()])
      except KeyError as error:
          print("[-] Cannot retrieve information about {}".format(self.target))

class Ignore(Op):
    def eval(self):
        pass
