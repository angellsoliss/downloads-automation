import os
import json

#load config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

#assign categories and what to skip from config
categories = config["Categories"]
skip = config["Skip"]

#rename file if shares the same name as another file in a folder
def duplicate_file(filename, folder):
    base, ext = os.path.splitext(filename)

    #increment counter for every duplicate
    counter = 1

    #check if newly downloaded file has the same name as an existing file in target folder
    while os.path.exists(os.path.join(folder, filename)):
        #if so, edit name of newly downloaded file
        filename = f"{base}_{counter}{ext}"
        counter += 1
    
    return filename

#formate file names, make them lowercase and replace spaces with underscores
def lowercase_extension(filename):
    name, ext = os.path.splitext(filename)
    if name and ext:
        adjusted_name = name + ext.lower()
        adjusted_name = adjusted_name.replace(' ', '_')  
        return adjusted_name

#create folders in download directory if they do not exist
def create_folders():
    pdf_folder = os.path.join(DOWNLOADS_FOLDER, 'PDFs')
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    img_folder = os.path.join(DOWNLOADS_FOLDER, 'Images')
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    video_folder = os.path.join(DOWNLOADS_FOLDER, 'Videos')
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    doc_folder = os.path.join(DOWNLOADS_FOLDER, 'Documents')
    if not os.path.exists(doc_folder):
        os.makedirs(doc_folder)

    music_folder = os.path.join(DOWNLOADS_FOLDER, 'Music')
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)

    prog_folder = os.path.join(DOWNLOADS_FOLDER, 'Programming')
    if not os.path.exists(prog_folder):
        os.makedirs(prog_folder)

    zip_folder = os.path.join(DOWNLOADS_FOLDER, 'Compressed_ZIPS')
    if not os.path.exists(zip_folder):
        os.makedirs(zip_folder)

    extracted_folder = os.path.join(DOWNLOADS_FOLDER, 'Extracted')
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)

    misc_folder = os.path.join(DOWNLOADS_FOLDER, 'Miscellaneous')
    if not os.path.exists(misc_folder):
        os.makedirs(misc_folder)  

#designate downloads folder/overhead
DOWNLOADS_FOLDER = (os.path.expanduser("~\Downloads"))
create_folders()
extracted = []

#iterate through compressed files, grab names
for file in os.listdir(os.path.join(DOWNLOADS_FOLDER, 'Compressed_ZIPS')):
    zip_name, ext = os.path.splitext(file)
    extracted.append(zip_name)

#adjust file names to lowercase and replace spaces with underscores first
for file in os.listdir(DOWNLOADS_FOLDER):
    #if file is not a directory
    if not os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file)):
        try:
            #adjust name
            adjusted_name = lowercase_extension(file)
            os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(DOWNLOADS_FOLDER, adjusted_name))
        except Exception as e:
            print(f"Error renaming file {file}: {e}")

#iterate through files in the downloads folder
for file in os.listdir(DOWNLOADS_FOLDER):
    #split file name and extension
    file_name, ext = os.path.splitext(file)

    #if file is an executable, skip
    if ext in config["Skip"]:
        continue

    #if file is a directory, check if it matches the name of a compressed file
    if os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file)):
        if file in extracted:
            extracted_folder = os.path.join(DOWNLOADS_FOLDER, 'Extracted')
            duplicate_file(file, extracted_folder)
            os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(extracted_folder, file))
        else:
            continue
    
    #flag to check if file has been moved
    moved = False

    #iterate through categories dictionary, save category and extension array
    for category, extensions in categories.items():

        #if file extension matches an extension in any of the valid categories
        if ext in extensions:
            #designate appropriate folder
            target_folder = os.path.join(DOWNLOADS_FOLDER, category)

            #save unique name
            unique_name = duplicate_file(file, os.path.join(DOWNLOADS_FOLDER, category))

            #move file to appropriate folder
            os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(target_folder, unique_name))

            moved = True

            #break loop since file has been moved, no need to check other categories
            break

    #if file has not been moved, then it belongs in misc
    if not moved:
        misc_folder = os.path.join(DOWNLOADS_FOLDER, 'Miscellaneous')
        unique_name = duplicate_file(file, misc_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(misc_folder, unique_name))

#troubleshooting
#print(extracted)