import os

def lowercase_extension(filename):
    name, ext = os.path.splitext(filename)
    if name and ext:
        adjusted_name = name + ext.lower()
        adjusted_name = adjusted_name.replace(' ', '_')  
        return adjusted_name

def create_folders():
    #create a folder for PDFs if it doesn't exist
    pdf_folder = os.path.join(DOWNLOADS_FOLDER, 'PDFs')
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    #same for images
    img_folder = os.path.join(DOWNLOADS_FOLDER, 'Images')
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    #same for videos
    video_folder = os.path.join(DOWNLOADS_FOLDER, 'Videos')
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    #same for documents
    doc_folder = os.path.join(DOWNLOADS_FOLDER, 'Documents')
    if not os.path.exists(doc_folder):
        os.makedirs(doc_folder)

    #same for music
    music_folder = os.path.join(DOWNLOADS_FOLDER, 'Music')
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)

    #same for programming files
    prog_folder = os.path.join(DOWNLOADS_FOLDER, 'Programming')
    if not os.path.exists(prog_folder):
        os.makedirs(prog_folder)
    
    #same for zips
    zip_folder = os.path.join(DOWNLOADS_FOLDER, 'Compressed')
    if not os.path.exists(zip_folder):
        os.makedirs(zip_folder)

    #same for miscellaneous files
    misc_folder = os.path.join(DOWNLOADS_FOLDER, 'Miscellaneous')
    if not os.path.exists(misc_folder):
        os.makedirs(misc_folder)  

#designate downloads folder
DOWNLOADS_FOLDER = (os.path.expanduser("~\Downloads"))

create_folders()

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

    #if file is a directory, skip
    if os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file)):
        continue

    #if file is a pdf
    elif file.endswith('.pdf'):
        #designate pdf folder
        pdf_folder = os.path.join(DOWNLOADS_FOLDER, 'PDFs')

        #move file from downloads folder to pdf folder by renaming it
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(pdf_folder, file))
    elif file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.heic', '.jfif', '.ico')):
        img_folder = os.path.join(DOWNLOADS_FOLDER, 'Images')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(img_folder, file))
    elif file.endswith(('.mp4', '.mov', '.avi', '.wmv', '.mkv', '.flv', '.webm')):
        video_folder = os.path.join(DOWNLOADS_FOLDER, 'Videos')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(video_folder, file))
    elif file.endswith(('.mp3', '.wav', '.aac', '.flac', '.aiff', '.wma', '.ogg', '.m4a', '.mid')):
        music_folder = os.path.join(DOWNLOADS_FOLDER, 'Music')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(music_folder, file))
    elif file.endswith(('.docx', '.doc', '.txt', '.csv', '.ppt', '.pptx', '.html', '.xlsx')):
        doc_folder = os.path.join(DOWNLOADS_FOLDER, 'Documents')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(doc_folder, file))
    elif file.endswith(('.py', '.js', '.java', '.cpp', '.c', '.cs', '.css', '.php', '.sql', '.asm')):
        prog_folder = os.path.join(DOWNLOADS_FOLDER, 'Programming')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(prog_folder, file))
    elif file.endswith(('.zip', '.tar', '.gz', '.rar', '.7z', '.bz2', '.xz')):
        zip_folder = os.path.join(DOWNLOADS_FOLDER, 'Compressed')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(zip_folder, file))
    else:
        misc_folder = os.path.join(DOWNLOADS_FOLDER, 'Miscellaneous')
        os.rename(os.path.join(DOWNLOADS_FOLDER, file), os.path.join(misc_folder, file))