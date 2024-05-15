import shutil

def create_report(template_name: str, report_name: str) -> None:

    template_file_path = f"./templates/{template_name}"
    report_file_path = f"./output/{report_name}"

    source_file =  open(template_file_path, 'rb')

    # you have to open the destination file in binary mode with 'wb'
    destination_file = open(report_file_path, 'wb')

    # use the shutil.copyobj() method to copy the contents of source_file to destination_file
    shutil.copyfileobj(source_file, destination_file)