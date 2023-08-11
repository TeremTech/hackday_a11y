import config
import shutil


def modify_line_in_report(line_num, new_content):
    # Create a temporary file
    with open("report.html", 'r') as file, open("temp.txt", 'w') as temp_file:
        for current_line_num, line in enumerate(file, 1):
            # If current line number is the one to modify, replace it
            if current_line_num == line_num:
                temp_file.write(new_content + '\n')
            else:
                temp_file.write(line)

    # Replace the original file with the modified temporary file
    shutil.move("temp.txt", "report.html")


def modify_cleanup():
    modify_progress(100)
    remove_remaining()
    shrink_progress()
    remove_refresh()


def remove_refresh():
    modify_line_in_report(6, '')


def remove_remaining():
    modify_line_in_report(116, '')


def shrink_progress():
    modify_line_in_report(45, "height: 10px;")


def modify_violations(num):
    modify_line_in_report(114, f"<tr><th>Total violations:</th><th>{num}</th></tr>")


def modify_processed(num):
    modify_line_in_report(115, f"<tr><th>Pages processed:</th><th>{num}</th></tr>")


def modify_remaining(num):
    modify_line_in_report(116, f"<tr><th>Pages remaining:</th><th>{num}</th></tr>")


def modify_progress(percentage):
    modify_line_in_report(118, f'<center><progress max="100" value="{percentage}"></progress></center>')
