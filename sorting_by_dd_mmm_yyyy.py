import os
import time
import shutil

# go to the correct folder
# os.chdir('Photos')

# go through the list of files
for file in os.listdir():

    # create the Date String dd Mon yyyy
    date = time.strftime('%d %b %Y', time.gmtime(os.path.getmtime(file)))
    collection_dir = date

    # if it is a folder do not read
    if os.path.isdir(file):
        continue

    # if a folder do not exist then create it with the Date string used as a name
    if not os.path.exists(collection_dir):
        os.mkdir(collection_dir)

    # if a file is not in a folder then copy it
    if not os.path.exists(collection_dir + '/' + file):
        shutil.copy2(file, collection_dir)
    else:
        counter = 0

        old_name = os.path.join(collection_dir, file)
        # get file name without extension
        only_name = os.path.splitext(file)[0]
        only_extension = os.path.splitext(file)[1]

        # read the Date filder and if counts how many similar files are there to add as a counter
        for f_name in os.listdir(collection_dir):
            if f_name.startswith(only_name):
                counter += 1

        # Adding the new name with extension
        new_base = only_name + '_copy(' + str(counter) + ')' + only_extension
        # construct full file path
        new_name = os.path.join(collection_dir, new_base)

        # Renaming the file
        os.rename(old_name, new_name)

        # copy a file with a new name
        shutil.copy2(file, collection_dir)
