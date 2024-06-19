# import os    !!!try at another place!!!
#
#
# def save_extensions(dir_name):
#     for file_name in os.listdir(dir_name):
#         file = os.path.join(dir_name, file_name)
#
#         if os.path.isfile(file):
#             extension = file.split(".")[-1]
#             extensions[extension] = extensions.get(extension, []) + [file_name]
#         elif os.path.isdir(file):
#             save_extensions(file)
#
#
# directory = input()
# extensions = {}
# save_extensions(directory)
# print(extensions)