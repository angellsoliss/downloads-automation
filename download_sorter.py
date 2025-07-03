import os

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
    #if file is an executable, skip
    if file.endswith(('.exe', '.bat', '.sh', '.cmd', '.msi', '.apk')):
        continue

    #if file is a directory, check if it matches the name of a compressed file
    if os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file)):
        if file in extracted:
            extracted_folder = os.path.join(DOWNLOADS_FOLDER, 'Extracted')
            duplicate_file(file, extracted_folder)
            os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(extracted_folder, file))
        else:
            continue

    #if file is a pdf
    elif file.endswith('.pdf'):
        #designate pdf folder
        pdf_folder = os.path.join(DOWNLOADS_FOLDER, 'PDFs')

        #check for duplicates in pdf folder
        #if file is not a duplicate, name will remain unchanged
        unique_name = duplicate_file(file, pdf_folder)

        #move file from downloads folder to pdf folder by renaming it
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(pdf_folder, unique_name))
    elif file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.heic', '.jfif', '.ico')):
        img_folder = os.path.join(DOWNLOADS_FOLDER, 'Images')
        unique_name = duplicate_file(file, img_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(img_folder, unique_name))
    elif file.endswith(('.mp4', '.mov', '.avi', '.wmv', '.mkv', '.flv', '.webm')):
        video_folder = os.path.join(DOWNLOADS_FOLDER, 'Videos')
        unique_name = duplicate_file(file, video_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(video_folder, unique_name))
    elif file.endswith(('.mp3', '.wav', '.aac', '.flac', '.aiff', '.wma', '.ogg', '.m4a', '.mid')):
        music_folder = os.path.join(DOWNLOADS_FOLDER, 'Music')
        unique_name = duplicate_file(file, music_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(music_folder, unique_name))
    elif file.endswith(('.docx', '.doc', '.txt', '.csv', '.ppt', '.pptx', '.html', '.xlsx')):
        doc_folder = os.path.join(DOWNLOADS_FOLDER, 'Documents')
        unique_name = duplicate_file(file, doc_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(doc_folder, unique_name))
    elif file.endswith(('.py', '.js', '.java', '.cpp', '.c', '.cs', '.css', '.php', '.sql', '.asm')):
        prog_folder = os.path.join(DOWNLOADS_FOLDER, 'Programming')
        unique_name = duplicate_file(file, prog_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(prog_folder, unique_name))
    elif file.endswith(('.zip', '.tar', '.gz', '.rar', '.7z', '.bz2', '.xz')):
        zip_folder = os.path.join(DOWNLOADS_FOLDER, 'Compressed_ZIPS')
        unique_name = duplicate_file(file, zip_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(zip_folder, unique_name))
    else:
        misc_folder = os.path.join(DOWNLOADS_FOLDER, 'Miscellaneous')
        unique_name = duplicate_file(file, misc_folder)
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(misc_folder, unique_name))

#troubleshooting
#print(extracted)