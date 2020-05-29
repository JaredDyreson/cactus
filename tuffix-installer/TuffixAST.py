from rply.token import BaseBox
from ClassInformation import class_information_map
from Fetch import fetch

"""
TODO:

- All functionality of the program should be here
- The functions Kevin writes should be imported into this file and assigned correctly
"""

class Target(BaseBox):
    def __init__(self, target):
        self.target = target

    def eval(self):
        """
        Simply display the selected target
        """

        print("Target: {}".format(self.target))
        return self.target

class Install(Target):
    def eval(self):
      """
      Run the corresponding Ansible target
      Naming scheme example should be:
      CPSC_121_AnsiblePlaybook.ansible
      """

      print("[+] Installing {}".format(self.target))
      print("[+] Running {}_AnisblePlaybook.ansible".format(self.target.replace("-", "_")))

class Remove(Target):
    def eval(self):
      """
      Remove the corresponding Ansible target
      Naming scheme example should be:
      CPSC_121_AnsiblePlaybook.ansible
      """

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

class Status(Target):
    def eval(self):
       print("----- BEGIN Information about host -----")
       fetch()
       print("----- END Information about host -----")
