import os
import time
import shutil
import base64
import zipfile
import subprocess
import random
import string
import sys
import json

output_folder = "variant"

class Color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m' # For console/terminal default color

# Preset of colored text for displaying on console/terminal
warning_label = f"{Color.YELLOW}Warning:{Color.RESET}"
error_label = f"{Color.RED}Error:{Color.RESET}"
success_label = f"{Color.GREEN}Success:{Color.RESET}"
info_label = f"{Color.BLUE}Info:{Color.RESET}"
tick_symbol = f"{Color.GREEN}[{"\u2713"}]{Color.RESET}"
cross_symbol = f"{Color.RED}[{"\u2717"}]{Color.RESET}"
# Will later use to join any relative path to create absolute path to prevent file does not exist
current_directory = os.getcwd()
debug = False

def check_output_folder(destination:str=output_folder):
    if(not os.path.exists(os.path.join(current_directory,destination))):
        print(warning_label,destination,"does not exist.")
        os.mkdir(os.path.join(current_directory,destination))
        print(success_label,f"Create directory {destination} successfully")

    else:
        if(debug):
            print(info_label,f"directory {destination} does exist.")

    return True

def check_replace(destination:str=output_folder):
    if(os.path.exists(os.path.join(current_directory,destination))):
        print(warning_label,f"file already exists at {destination}, it will be replaced")
        return True
    return False

def rename_file(input_file:str,output_file:str,keep_original:bool=True):
    print()
    header = "===== Rename File ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,output_file)
    
    if(not os.path.exists(input_file)):
        print(error_label,f"{input_file} does not exist")
        return False
    
    check_replace(output_file)
    shutil.copy(input_file,output_file)
    print(success_label,f"create file at {output_file} successfully")

    if(not keep_original):
        os.remove(input_file)
        print(success_label,f"remove original file {filename} successfully")

    if(debug):
        print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")

    print("="*len(header))
    print()
    return True

def base64_encode(input_file:str,keep_original:bool=True):
    print()
    header = "===== Base64 Encode ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"base64_encoded_{filename}")

    check_replace(output_file)
    try:
        with open(input_file,"rb") as f:
            encoded = base64.b64encode(f.read())
            print(success_label,f"read file {filename} successfully")

        with open(output_file,"wb") as f:
            f.write(encoded)
            print(success_label,f"save file at {output_file} successfully")

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {filename} successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")

        print("="*len(header))
        print()
        return True
                
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def base64_decode(input_file:str,keep_original:bool=True):
    print()
    header = "===== Base64 Decode ===="
    print("header")
    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"base64_decoded_{filename}")

    check_replace(output_file)
    try:
        with open(input_file,"rb") as f:
            encoded = base64.b64decode(f.read())
            print(success_label,f"read file {filename} successfully")

        with open(output_file,"wb") as f:
            f.write(encoded)
            print(success_label,f"save file at {output_file} successfully")

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {filename} successfully")


        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")

        print("="*len(header))
        print()
        return True
            
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def ceasar_cipher_encrypt(input_file:str,ROT:int=13,keep_original:bool=True):
    print()
    header = "===== Ceasar Cipher shift-{ROT} encrypt ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"ROT{ROT}_encrypted_{filename}")

    check_replace(output_file)
    try:
        encrypted_content = bytearray()
        with open(input_file,"rb") as f:
            content = f.read()
            print(success_label,f"read file {filename} successfully")
            
            for byte in content:
                encrypted_byte = (byte + ROT) % 256  
                encrypted_content.append(encrypted_byte)

            print(success_label,f"encrypt with shift {ROT} of {filename} successfully")

        with open(output_file,"wb") as f:
            f.write(encrypted_content)
            print(success_label,f"save file at {output_file} successfully")

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {filename} successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def ceasar_cipher_decrypt(input_file:str,ROT:int=13,keep_original:bool=True):
    print()
    header = "===== Ceasar Cipher shift-{ROT} decrypt ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"ROT{ROT}_decrypted_{filename}")

    check_replace(output_file)
    try:
        encrypted_content = bytearray()
        with open(input_file,"rb") as f:
            content = f.read()
            print(success_label,f"read file {filename} successfully")
            
            for byte in content:
                encrypted_byte = (byte - ROT) % 256  
                encrypted_content.append(encrypted_byte)

            print(success_label,f"decrypt with shift {ROT} of {filename} successfully")

        with open(output_file,"wb") as f:
            f.write(encrypted_content)
            print(success_label,f"save file at {output_file} successfully")

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {filename} successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")

        print("="*len(header))
        print()
        return True
            
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def file_partition(input_file:str,output_dir:str,partition:int=10,keep_original:bool=True):
    print()
    header = "===== Divide file into {partition} partitions ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    if(partition <= 0):
        raise Exception(f"Number of partition ({partition}) is invalid. Should be positive integer")
    
    check_output_folder()

    try:
        with open(input_file, 'rb') as f:
            # Read the entire content of the input file
            content = f.read()
            file_size = f.seek(0, 2)  
            file_size = f.tell()
            print(success_label,f"read file {input_file} successfully")

        if(partition > file_size):
            raise Exception(f"number of partition ({partition}) exceeds file size {file_size}")

        check_output_folder(f"{output_folder}/{output_dir}")

        partition_size = (len(content) + partition - 1) // partition
        for i in range(partition):
            partition_filename = os.path.join(current_directory, f'{output_folder}/{output_dir}/{input_file}_part{i+1}')
            start = i * partition_size
            end = min((i + 1) * partition_size, len(content))
            check_replace(partition_filename)
            with open(partition_filename, 'wb') as f:
                f.write(content[start:end])
                if(debug):
                    print(info_label,f"successfully write {partition_filename}")

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {input_file} successfully")

        print(success_label,f"successfully partition file {input_file}")
        print(success_label,f"files are saved at {output_dir}")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
    
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def combine_partition(input_dir:str,partition:int=10,keep_original=False):
    print()
    header = f"===== Combine {partition} partitions ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    if(partition <= 0):
        raise Exception(f"Number of partition ({partition}) is invalid. Should be positive integer")
    
    check_output_folder()
    input_dir = os.path.join(current_directory,input_dir)

    total_partition = os.listdir(input_dir)
    filename = (total_partition[0].rsplit("_",1))[0]
    output_file = os.path.join(output_folder,filename)
    check_replace(output_file)

    if(debug):
        print(info_label,f"found file {filename} on {input_dir}")

    try:
        if(len(total_partition) != partition):
            raise Exception(f"The partitions on directory ({len(total_partition)}) does not match specified ({partition})")
        
        else:
            if(debug):
                print(info_label,"number of partition is matched")

        for i in range(1,partition+1):
            partition_file = os.path.join(input_dir,f"{filename}_part{i}")
            if(not os.path.exists):
                raise Exception(f"{partition_file} is missing.")
            
            with open(partition_file,"rb") as fr:
                if(debug):
                    print(success_label,f"read file {partition_file} successfully")
                with open(output_file,"ab") as fw:
                    fw.write(fr.read())
                    if(debug):
                        print(success_label,f"append part{i} to {output_file} successfully.")

        if(not keep_original):
            for i in range(1,partition+1):
                partition_file = os.path.join(input_dir,f"{filename}_part{i}")
                os.remove(partition_file)
                if(debug):
                    print(warning_label,f"{partition_file} is removed.")

            os.removedirs(input_dir)
 
        print(success_label,f"combine file {output_file} successfully.")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def add_leading(input_file:str,byte_to_add:bytes=b"ZZ",keep_original=True):
    print()
    header = f"===== add leading byte ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"add_leading_{filename}")
    check_replace(output_file)

    try:
        with open(input_file,"rb") as fr:
            if(debug):
                print(success_label,f"read file {filename} successfully.")
            with open(output_file,"wb") as fw:
                fw.write(byte_to_add+fr.read())

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {input_file} successfully")

        print(success_label,f"add leading string and save as {input_file} successfully")
        
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def remove_leading(input_file:str,byte_to_remove:bytes=b"ZZ",keep_original=True):
    print()
    header = f"===== remove leading byte ====="
    print(header)

    if(debug):
        start_time = time.time()
    
    check_output_folder()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    output_file = os.path.join(current_directory,output_folder,f"remove_leading_{filename}")
    check_replace(output_file)

    try:
        with open(input_file,"rb") as fr:
            if(debug):
                print(success_label,f"read file {input_file} successfully.")
            content = fr.read()
            location_leading = content.find(byte_to_remove)
            if(debug):
                print(info_label,f"location of leading string is {location_leading}")
            if(location_leading == -1 or location_leading > 0):
                raise Exception(warning_label,f"Provided leading bytes do not exist on {filename}")
                
            content = content[len(byte_to_remove):]

            with open(output_file,"wb") as fw:
                fw.write(content)

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file successfully")

        print(success_label,f"remove leading string and save as {filename} successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def create_zip(input_file: str, zip_layer: int = 1, keep_original = True):

    print()
    header = f"===== Zip file {zip_layer} nested zip ====="
    print(header)

    if(debug):
        start_time = time.time()

    if(not os.path.exists(os.path.join(current_directory,input_file))):
        print(error_label,f"{input_file} does not exist")
        return False
    
    output_file = f"{os.path.basename(input_file)}.zip"  
    check_output_folder()
    check_replace(os.path.join(current_directory,output_folder,f"{input_file}.zip"))

    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as f:
            f.write(input_file)

        if(debug):
            print(success_label,f"Nested-1 zip of {input_file} successfully")
        count = 2
        for _ in range(zip_layer - 1):
            output_file = f"{os.path.basename(output_file)}.zip"  
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as f:
                f.write(output_file[:-4]) 
            os.remove(output_file[:-4])
            if(debug):
                print(success_label,f"Nested-{count} zip of {input_file} successfully")
                count+=1

        shutil.move(os.path.join(current_directory,output_file),os.path.join(current_directory,output_folder,f"{input_file}.zip"))

        if(not keep_original):
            os.remove(input_file)
            print(success_label,f"remove original file {input_file} successfully")

        print(success_label,f"Nested-{zip_layer} zip of {input_file} is created successfully")
        
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
    
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        print("="*len(header))
        print()
        return False

def compress(input_file:str,compressor:str="upx.exe",keep_original=True):
    print()
    header = f"===== compress with {compressor.split(".")[0]}  ====="
    print(header)

    if(debug):
        start_time = time.time()

    filename=  input_file
    check_output_folder()
    input_file = os.path.join(current_directory,input_file)
    command = [f'./{compressor}', "-k",input_file]
    check_replace(os.path.join(current_directory,output_folder,f"compressed_{filename}"))
    try:
        command = subprocess.run(command, capture_output=True, text=True)
        if(debug):
            print(command.stdout)

        if(not command.stderr):
            shutil.move(input_file, os.path.join(current_directory,output_folder,f"compressed_{filename}"))
            backup_name = input_file[:-1] + "~"
            shutil.move(backup_name,filename)

            if(not keep_original):
                os.remove(os.path.join(current_directory,filename))
                print(success_label,f"remove original file {input_file} successfully")

            print(success_label,f"Compress {input_file} successfully")
        else:
            raise Exception(command.stderr)
        
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return False
        
def pad_file(input_file:str, target_size:int = 10 * 1024 * 1024, keep_original=True):

    print()
    header = f"===== padding file to {target_size/1024**2:.2f} MB  ====="
    print(header)

    if(debug):
        start_time = time.time()

    filename = input_file
    check_output_folder()
    input_file = os.path.join(input_file)
    if(not os.path.exists(input_file)):
        print(error_label,f"{input_file} does not exist")
        return False

    current_size = os.path.getsize(input_file)
    padding_size = target_size - current_size
    if padding_size <= 0:
        print("File is already equal to or larger than the target size.")
        return

    variant_path = os.path.join(current_directory,output_folder,f"padded_{filename}")
    check_replace(variant_path)

    try:
        if(not keep_original):
            shutil.move(input_file,variant_path)
            
        else:
            shutil.copy(input_file,variant_path)
        
        with open(variant_path, 'ab') as f:
            f.write(b'\x00' * padding_size)
            print(success_label,"padding successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True

    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return False
    
def merge_with(input_file:str,merge_file:str):

    print()
    header = f"===== Merge with another file  ====="
    print(header)

    if(debug):
        start_time = time.time()

    filename = input_file
    mergename = merge_file

    check_output_folder()
    input_file = os.path.join(current_directory,input_file)
    merge_file = os.path.join (merge_file)

    try:
        with open(merge_file, 'rb') as image_file:
            merge_data = image_file.read()
            print(success_label,f"Read stage file {merge_file} successfully")
        
        # Read the content of the file to merge
        with open(input_file, 'rb') as file_to_merge:
            file_data = file_to_merge.read()
            print(success_label,f"Read file to be hidden {input_file} successfully")

        # Concatenate the data
        merge_data = merge_data + file_data
        if("." in merge_file):
            filename = filename + "."+merge_file.rsplit(".",1)[1]

        output_path = os.path.join(current_directory,output_folder,f"merged_{filename}")
        check_replace(output_path)

        # Write the merged data to the output file
        with open(output_path, 'wb') as output_file:
            output_file.write(merge_data)

        # Add metadata to indicate the position of the hidden file
        hidden_file_start = len(file_data)
        metadata = f"Hidden file starts at byte {hidden_file_start}".encode()
        with open(output_path, 'ab') as output_file:
            output_file.write(metadata)
            print(success_label,f"Merge {input_file} with {mergename} successfully")

        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms") 
        print("="*len(header))
        print()
        return False

def magic_byte(input_file,magic_dict= {
    "pdf": "255044462D312E30",  # PDF magic byte
    "zip": "504B0304",          # ZIP magic byte
    "docx": "504B0304",         # DOCX magic byte (same as ZIP)
    "jpg": "FFD8FFE0",          # JPG magic byte
    "txt": "EFBBBF"             # TXT magic byte
},keep_original=True):
    print()
    header = f"===== Magic Byte Modifier  ====="
    print(header)

    if(debug):
        start_time = time.time()
    filename = input_file
    input_file = os.path.join(current_directory,input_file)
    print(warning_label,"This method support only exe file at this moment.")

    try:
        with open(input_file, 'rb') as f:
            content = bytearray(f.read())
            if(debug):
                print(success_label,f"read file {input_file} successfully")

        if(b"MZ" in content[:10]):
        
            for file_extension,magic in magic_dict.items():
                content_magic = content.copy()
                content_magic[:2] = bytearray.fromhex(magic)
                with open(os.path.join(current_directory,output_folder,f"{file_extension}_{filename}"),"wb") as f:
                    f.write(content_magic)
                print(success_label,f"change magic byte to {file_extension} successfully.")

            if(not keep_original):
                os.remove(input_file)
                print(success_label,f"remove original file {input_file} successfully")

        else:
            raise Exception("The provided file is not exe")
        
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return True
    
    except Exception as e:
        print(error_label,e)
        if(debug):
            print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")
        
        print("="*len(header))
        print()
        return False

def generate_all(input_file:str):
    start_time = time.time()
    chars = string.ascii_letters + string.digits
    random_filename = ''.join(random.choice(chars) for _ in range(10))
    random_extension = ''.join(random.choice(chars) for _ in range(3))
    random_filename = random_filename + "." + random_extension
    filename = input_file

    track_dict = {
        "rename file":rename_file(input_file,random_filename),
        "base64 encode":base64_encode(input_file),
        "ceasar cipher":ceasar_cipher_encrypt(input_file),
        "file partition":file_partition(input_file,f"partitioned_{filename}"),
        "add leading byte":add_leading(input_file),
        "create nested zip":create_zip(input_file,3),
        "compress with UPX":compress(input_file),
        "padding file with junk":pad_file(input_file),
        "alternate magic byte":magic_byte(input_file),
        "merge with another file":merge_with(input_file,"steg_image.jpg")
    }

    print()
    header = f"============ Summarize  ============"
    print(header)
        
    for keys,values in track_dict.items():
        if(values):
            print(f"{keys:<30}\t{tick_symbol}")
        else:
            print(f"{keys:<30}\t{cross_symbol}")

    print()
    if(debug):
        print(info_label,f"total execution time is {(time.time() - start_time)*1000:.2f} ms")

    print("="*len(header))
    print()
    
arguments = sys.argv
manual_doc = {
    "header":f"""{Color.GREEN}-h{Color.RESET} for show command manual for all function
{Color.GREEN}-h <function_name:str>{Color.RESET} for show command manual for a specified function
{Color.GREEN}-debug{Color.RESET} for show debugging result
          
{Color.BOLD}<any thing:data_type>{Color.RESET} means this arguments are compulsory
[any thing:data_type=default_value] means this arguments are optional

{Color.RED}you are no need to specify argument name{Color.RESET}, just {Color.BOLD}directly place the values{Color.RESET} into the given placeholders.
""",
    "rename":f"""

{Color.BLUE}{Color.BOLD}===== Rename file ====={Color.RESET}
{Color.GREEN}-rename_file {Color.BOLD}<input_file_path:str>{Color.RESET} <output_file_path:str> [keep_original:bool=True]

This function is used to rename any file
""",
    "base64_encode":f"""
{Color.BLUE}{Color.BOLD}===== Base64 Encode ====={Color.RESET}
{Color.GREEN}-base64_encode {Color.BOLD}<input_file_path:str>{Color.RESET} [keep_original:bool=True]

This function is used to encode a file into base64 format
""",
    "base64_decode":f"""
{Color.BLUE}{Color.BOLD}===== Base64 Decode ====={Color.RESET}
{Color.GREEN}-base64_decode {Color.BOLD}<input_file:str>{Color.RESET} [keep_original:bool=True]

This function is used to decode a base64-encoded file
""",
    "ceasar_encrypt":f"""
{Color.BLUE}{Color.BOLD}===== Ceasar Cipher Encrypt ====={Color.RESET}
{Color.GREEN}-ceasar_cipher_enc {Color.BOLD}<input_file_path:str>{Color.RESET} [rotate:int=13] [keep_original:bool=True]

This function is used to apply Ceasar Cipher encryption with customized rotation
""",
    "ceasar_decrypt":f"""
{Color.BLUE}{Color.BOLD}===== Ceasar Cipher Decrypt ====={Color.RESET}
{Color.GREEN}-ceasar_cipher_enc {Color.BOLD}<input_file_path:str>{Color.RESET} [rotate:int=13] [keep_original:bool=True]

This function is used to apply Ceasar Cipher decryption with customized rotation  
""",
    "partition":f"""
{Color.BLUE}{Color.BOLD}===== Partition ====={Color.RESET}
{Color.GREEN}-file_partition {Color.BOLD}<input_file:str> <output_dir:str>{Color.RESET} [partition:int=10] [keep_original:bool=True]

This function is used to partition file into customized pieces. output_dir means the output directory. The partitioned files' name will end with _part<number>
""",
    "combine":f"""
{Color.BLUE}{Color.BOLD}===== combine partition ====={Color.RESET}
{Color.GREEN}-combine_partition {Color.BOLD}<input_dir:str>{Color.RESET} [partition:int=10] [keep_original:bool=True]

This function is used to combine partitioned file. input_dir mean the input directory that stores file partitions The partition file should end with _part<number>.
""",
    "add_leading":f"""
{Color.BLUE}{Color.BOLD}===== Add Leading ====={Color.RESET}
{Color.GREEN}-add_leading {Color.BOLD}<input_file:str>{Color.RESET} [byte_to_add:bytes=b"ZZ"] [keep_original:bool=True]

This function is used to add any bytes in the start of the file. byte_to_add should be in byte such as "ABC" or "/x01" or "/u1231"
""",
    "remove_leading":f"""
{Color.BLUE}{Color.BOLD}===== remove leading ====={Color.RESET}
{Color.GREEN}-remove_leading {Color.BOLD}<input_file:str>{Color.RESET} [byte_to_remove:bytes=b"ZZ"] [keep_original:bool=True]

This function will remove the leading bytes appeared in the start of the file. byte_to_add should be in Python byte formant not string for example b"Hello" not "Hello".
""",
    "create_zip":f"""
{Color.BLUE}{Color.BOLD}===== create zip ====={Color.RESET}
{Color.GREEN}-create_zip {Color.BOLD}<input_file:str>{Color.RESET} [zip_layer:int=1] [keep_original:bool=True]

This function is used to created recursive zipped file with customized recursive level.
""",
    "compress":f"""
====={Color.RESET}
{Color.GREEN}-compress {Color.BOLD}<input_file:str>{Color.RESET} [ compressor:str="upx.exe"] [keep_original=True]

Currently, this function will use {Color.BOLD}UPX compressor{Color.RESET} to compress any compressable file (e.g. exe or PE file). The compressed file can be executed even it does not be extracted. 
""",
    "padding":f"""
{Color.BLUE}{Color.BOLD}===== file padding ====={Color.RESET}
{Color.GREEN}-pad {Color.BOLD}<input_file:str>{Color.RESET} [size_in_byte:int=10485760] [keep_original=True]

This function is used to pad file to be in larger size. The default padding size (size_in_byte) is set to 10 MB.
""",
    "merge":f"""
{Color.BLUE}{Color.BOLD}===== merge ====={Color.RESET}
{Color.GREEN}-merge {Color.BOLD}<input_file:str> <stage_file:str>{Color.RESET}

This function is use to hide <input_file> into <stage_file>. {Color.BOLD}Note:{Color.RESET} If you hide this file on image file, the image is still openable
""",
    "magic":f"""
{Color.BLUE}{Color.BOLD}===== magic byte modification ====={Color.RESET}
{Color.GREEN}-magic {Color.BOLD}<input_file:str>{Color.RESET} [magic_dict:dict[file_ext->magic_byte_hex]] [keep_original:True]

This function is use to manipulate magic bytes of file. {Color.YELLOW}Currently, I can support only exe file.{Color.RESET} 
The magic_dict is dictionary that should be in this format {{'pdf':'255044462D312E30','zip':'504B0304'}}
{Color.BOLD}Note: {Color.CYAN}Please use single quotes instead of double quotes.{Color.RESET}
The default magic byte dictionary is
    {{
        "pdf": "255044462D312E30",  # PDF magic byte
        "zip": "504B0304",          # ZIP magic byte
        "docx": "504B0304",         # DOCX magic byte (same as ZIP)
        "jpg": "FFD8FFE0",          # JPG magic byte
        "txt": "EFBBBF"             # TXT magic byte
    }}
""",
    "all":f"""
{Color.BLUE}{Color.BOLD}===== generate all ====={Color.RESET}
{Color.GREEN}-all {Color.BOLD}<input_file:str>{Color.RESET}

This funtion is used to generate all possible variants of input file   
"""
}
if(len(arguments) == 1):
    print(f"{Color.BOLD}=====================================================================")
    print(rf"""
 {Color.RED}__      __             _____    _____              _   _   _______ 
 {Color.YELLOW}\ \    / /     /\     |  __ \  |_   _|     /\     | \ | | |__   __|
  {Color.GREEN}\ \  / /     /  \    | |__) |   | |      /  \    |  \| |    | |   
   {Color.CYAN}\ \/ /     / /\ \   |  _  /    | |     / /\ \   | . ` |    | |   
    {Color.BLUE}\  /     / ____ \  | | \ \   _| |_   / ____ \  | |\  |    | |   
     {Color.PURPLE}\/     /_/    \_\ |_|  \_\ |_____| /_/    \_\ |_| \_|    |_|                                                                                                                         
    {Color.RESET}""")
    print(Color.RESET)
    print(f"{Color.BOLD}-h or --help for manual{Color.RESET}")
    print()
    print(f"Contributed by {Color.CYAN}@bluedegard/@AekanutOak")
    print(f"This code is {Color.GREEN}open-source{Color.RESET}, you can use, pull, or modify what ever you want!")
    print()
    print(f"{Color.BOLD}====================================================================={Color.RESET}")

elif("-h" in arguments or "--help" in arguments):
    if("rename" in arguments or "-rename" in arguments):
        print(manual_doc["rename"])
    elif("-base64_encode" in arguments or "base64_encode" in arguments):
        print(manual_doc["base64_encode"])
    elif("-base64_decode" in arguments or "base64_decode" in arguments):
        print(manual_doc["base64_decode"])
    elif("-ceasar_cipher_enc" in arguments or "ceasar_cipher_enc" in arguments):
        print(manual_doc["ceasar_encrypt"])
    elif("-ceasar_cipher_dec" in arguments or "ceasar_cipher_dec" in arguments):
        print(manual_doc["ceasar_decrypt"])
    elif("-file_partition" in arguments or "file_partition" in arguments):
        print(manual_doc["partition"])
    elif("-combine_partition" in arguments or "combine_partition" in arguments):
        print(manual_doc["combine"])
    elif("-add_leading" in arguments or "add_leading" in arguments):
        print(manual_doc["add_leading"])
    elif("-remove_leading" in arguments or "remove_leading" in arguments):
        print(manual_doc["remove_leading"])
    elif("-create_zip" in arguments or "create_zip" in arguments):
        print(manual_doc["create_zip"])
    elif("-compress" in arguments or "compress" in arguments):
        print(manual_doc["compress"])
    elif("-pad" in arguments or "pad" in arguments):
        print(manual_doc["padding"])
    elif("-merge" in arguments or "merge" in arguments):
        print(manual_doc["merge"])
    elif("-magic" in arguments or "magic" in arguments):
        print(manual_doc["magic"])
    elif("-all" in arguments or "all" in arguments):
        print(manual_doc["all"])
    else:
        for keys,values in manual_doc.items():
            print(values)
    
elif(len(arguments) > 1):
    if("-debug" in arguments):
        debug = True
        arguments.remove("-debug")
        
    if("-all" in arguments and len(arguments) == 3):
        generate_all(arguments[2])
 
    if("-rename_file" in arguments and len(arguments) < 6):
        print(len(arguments))
        if(len(arguments) == 4):
            rename_file(arguments[2],arguments[3])
            
        elif(len(arguments) == 5):
            if(arguments[4].lower() == "false"):
                arguments[4] = False
            rename_file(arguments[2],arguments[3],arguments[4])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-base64_encode" in arguments and len(arguments) < 5):
        if(len(arguments) == 3):
            base64_encode(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].lower() == "false"):
                arguments[3] = False
            base64_encode(arguments[2],arguments[3])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-base64_decode" in arguments and len(arguments) < 5):
        if(len(arguments) == 3):
            base64_decode(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].lower() == "false"):
                arguments[3] = False
            base64_decode(arguments[2],arguments[3])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-ceasar_cipher_enc" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            ceasar_cipher_encrypt(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                ceasar_cipher_encrypt(arguments[2],arguments[3])
            else:
                print(error_label,f"rotation should be integer not {arguments[3]}")

        elif(len(arguments) == 5):
            arguments[3] = int(arguments[3])
            if(arguments[4].lower() == "false"):
                arguments[4] = False
            ceasar_cipher_encrypt(arguments[2],arguments[3],arguments[4])
        else:
            print(error_label,"The command is invalid, please check manual")
    
    elif("-ceasar_cipher_dec" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            ceasar_cipher_decrypt(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                ceasar_cipher_decrypt(arguments[2],arguments[3])
            else:
                print(error_label,f"rotation should be integer but get {arguments[3]}")
        elif(len(arguments) == 5):
            arguments[3] = int(arguments[3])
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                ceasar_cipher_decrypt(arguments[2],arguments[3])
                if(arguments[4].lower() == "false"):
                    arguments[4] = False

                ceasar_cipher_decrypt(arguments[2],arguments[3],arguments[4])
            else:
                print(error_label,f"rotation should be integer but get {arguments[3]}")
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-file_partition" in arguments and len(arguments) < 7):
        if(len(arguments) == 4):
            file_partition(arguments[2],arguments[3])
        elif(len(arguments) == 5):
            if(arguments[4].isdigit()):
                arguments[4] = int(arguments[4])
                file_partition(arguments[2],arguments[3],arguments[4])
            else:
                print(error_label,f"number of partition should be integer but get {arguments[4]}")

        elif(len(arguments) == 6):
            if(arguments[4].isdigit()):
                arguments[4] = int(arguments[4])
                if(arguments[5].lower() == "false"):
                    arguments[5] = False
                file_partition(arguments[2],arguments[3],arguments[4],arguments[5])
            else:
                print(error_label,f"number of partition should be integer but get {arguments[4]}")
        else:
            print(error_label,"The command is invalid, please check manual")
    
    elif("-combine_partition" in arguments and len(arguments) < 6):
        print(len(arguments))
        if(len(arguments) == 3):
            combine_partition(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                combine_partition(arguments[2],arguments[3])   
            else:
                print(error_label,f"number of partition should be integer but get {arguments[4]}")

        elif(len(arguments) == 5):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                if(arguments[4].lower() == "false"):
                    arguments[4] = False
                combine_partition(arguments[2],arguments[3],arguments[4])   

            else:
                print(error_label,f"number of partition should be integer but get {arguments[4]}")
        else:
            print(error_label,"The command is invalid, please check manual")
    
    elif("-add_leading" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            add_leading(arguments[2])
        elif(len(arguments) == 4):
            arguments[3] = arguments[3].encode()
            add_leading(arguments[2],arguments[3])
        elif(len(arguments) == 5):
            arguments[3] = arguments[3].encode()
            if(arguments[4].lower() == "false"):
                arguments[4] = False
            add_leading(arguments[2],arguments[3],arguments[4])
        else:
            print(error_label,"The command is invalid, please check manual")
    
    elif("-remove_leading" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            remove_leading(arguments[2])
        elif(len(arguments) == 4):
            arguments[3] = arguments[3].encode()
            remove_leading(arguments[2],arguments[3])
        elif(len(arguments) == 5):
            arguments[3] = arguments[3].encode()
            if(arguments[4].lower() == "false"):
                arguments[4] = False
            remove_leading(arguments[2],arguments[3],arguments[4])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-create_zip" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            create_zip(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                create_zip(arguments[2],arguments[3])
            else:
                print(error_label,f"Number of nested should be integer not {arguments[3]}")

        elif(len(arguments) == 5):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                if(arguments[4].lower() == "false"):
                    arguments[4] = False
                create_zip(arguments[2],arguments[3],arguments[4])
            else:
                print(error_label,f"Number of nested should be integer not {arguments[3]}")
        
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-pad" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            pad_file(arguments[2])
        elif(len(arguments) == 4):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                pad_file(arguments[2],arguments[3])
            else:
                print(error_label,f"file size (bytes) should be integer not {arguments[3]}")

        elif(len(arguments) == 5):
            if(arguments[3].isdigit()):
                arguments[3] = int(arguments[3])
                if(arguments[4].lower() == "false"):
                    arguments[4] = False
                pad_file(arguments[2],arguments[3],arguments[4])
            else:
                print(error_label,f"file size (bytes) should be integer not {arguments[3]}")
        
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-compress" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            compress(arguments[2])
        elif(len(arguments) == 4):
            compress(arguments[2],arguments[3])
        elif(len(arguments) == 5):
            if(arguments[4].lower() == "false"):
                arguments[4] = False
            compress(arguments[2],arguments[3],arguments[4])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-merge" in arguments and len(arguments) < 5):
        if(len(arguments) == 4):
            merge_with(arguments[2],arguments[3])
        else:
            print(error_label,"The command is invalid, please check manual")

    elif("-magic" in arguments and len(arguments) < 6):
        if(len(arguments) == 3):
            magic_byte(arguments[2])
        elif(len(arguments) == 4):
            try:
                arguments[3] = arguments[3].replace("'","\"")
                arguments[3] = json.loads(arguments[3])
                magic_byte(arguments[2],arguments[3])
            except Exception as e:
                print(error_label,"Magic byte dictionary is invalid, please use single quote for key and value",e)
        
        elif(len(arguments) == 5):
            try:
                arguments[3] = arguments[3].replace("'","\"")
                arguments[3] = json.loads(arguments[3])
                if(arguments[4].lower() == "false"):
                    arguments[4] = False
                magic_byte(arguments[2],arguments[3],arguments[4])
            except Exception as e:
                print(error_label,"Magic byte dictionary is invalid, please use single quote for key and value",e)

        else:
            print(error_label,"The command is invalid, please check manual")
    else:
            print(error_label,"The command is invalid, please check manual")

