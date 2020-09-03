import os
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
      full_name = os.path.join(root, name)
      with open(full_name) as myfile:
          lines=myfile.read()
          print(lines)