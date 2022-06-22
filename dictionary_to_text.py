import emoji



def format_value(v, indent):
    if isinstance(v, list):
         return ''.join([format_value(item, indent) for item in v])
    elif isinstance(v, dict):
         return format_dict(v, indent)
    elif isinstance(v, str):
         return (" " * indent) + v + "\n"

def format_dict(d, indent=0):
    res = ""
    for key in d:
        res += ("   " * indent) + key + ":"
        res += format_value(d[key], indent + 1)
    return res


attendance_status = emoji.emojize(':thumbs_up:').encode('utf-8')
# employee_name = "Ejiro"
# employee_name_status = "Employee_name"
# employee_attendance_status = "Attendance_status"
# attendant = {
#         employee_attendance_status: attendance_status
#         }
# attendnce2 = {
#      employee_name_status: employee_name} 

# a = format_dict(attendnce2)
# b  = format_dict(attendant)
# c  = b + a 
print(attendance_status)