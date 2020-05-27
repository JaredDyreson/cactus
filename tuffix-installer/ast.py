from rply.token import BaseBox
from ClassInformation import class_information_map

class Target(BaseBox):
    def __init__(self, target):
        self.target = target

    def eval(self):
        print("Target: {}".format(self.target))
        return self.target

class Install(Target):
    def eval(self):
      print("[+] Installing {}".format(self.target))

class Remove(Target):
    def eval(self):
      print("[+] Removing {}".format(self.target))

class Describe(Target):
    def eval(self):
      try:
          print("[+] Information about {}".format(self.target))
          print(class_information_map[self.target.lower()])
      except KeyError as error:
          print("[-] Cannot retrieve information about {}".format(self.target))

class Ignore(Target):
    def eval(self):
        pass
