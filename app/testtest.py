from django.conf import settings
import os
settings.configure()

test_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_directory = "/media"
dir_list = []
file_list = []
if os.path.isdir(test_directory):
        for child in os.listdir(test_directory):
            test_path = os.path.join(test_directory, child)
            if os.path.isdir(test_path):
                dir_list.append(child)
            else:
                file_list.append(child)

print(dir_list)
print(file_list)
