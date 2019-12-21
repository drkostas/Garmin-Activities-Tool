import os
import re

print
print
print "3.    H E A D E R    C L E A N E R"
print
print "(For any request/help email me @ \"georgiou.kostas@hotmail.com\")"
print

step = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
tcx_inputs = dir_path+"/Inputs/TCX/"
welder_inputs = dir_path+"/Inputs/GpxTcxWelder/"
welder_outputs = dir_path+"/Outputs/GpxTcxWelder/"
print "\nList of all tcx files in the Inputs/TCX Directory:"
for file in os.listdir(tcx_inputs):
    if file.endswith(".tcx"):
        print(os.path.join(tcx_inputs, file))

tcxname = raw_input("\nPlease give the name of your initial tcx file: ")

print "\nList of all tcx files in the Inputs/GpxTcxWelder Directory:"
for file in os.listdir(welder_inputs):
    if file.endswith(".tcx"):
        print(os.path.join(welder_inputs, file))

welder_inputs = dir_path+"/Inputs/GpxTcxWelder/"
weldername = raw_input("\nPlease give the tcx filename you exported from GpxTcxWelder: ")


activityType = raw_input("\nIs your activity swimming (y/n)? ")
if (activityType != "y" and activityType != "n"):
	while (activityType != "y" and activityType != "n"):
		print "Wrong input. Please press y or n."
		activityType = raw_input("\nIs your activity swimming (y/n)? ")

tcx_content = open(tcx_inputs+tcxname, 'r').read()
welder_content = open(welder_inputs+weldername, 'r').read()
tcx_header = re.findall(r"<TrainingCenterDatabase.*?>",tcx_content,re.MULTILINE|re.DOTALL)
new_welder_content = re.sub(r"<TrainingCenterDatabase.*?>", tcx_header[0], welder_content,flags=re.MULTILINE|re.DOTALL)
if activityType == "y":
	new_welder_content = re.sub(r"<Activity Sport=\".*\">", "<Activity Sport=\"Swimming\">", new_welder_content,flags=re.MULTILINE)

fileToSave = open(welder_outputs+'EDITED_' + weldername, 'w')
fileToSave.write(new_welder_content)
print
print "File Saved Succesfully."
print
print "Your file is in \"Outputs/GpxTcxWelder\" and it\'s now ready to be imported in any Fitness Tracking website!!"

