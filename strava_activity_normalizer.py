import os
import re

def normalize(match):
	dist = match.group(2)
	dist = float(dist) * actual_dist/rec_dist
	return match.group(1) + str(dist) + match.group(3)

dir_path = os.path.dirname(os.path.realpath(__file__))
print "\nList of all tcx files in this Directory:"
for file in os.listdir(dir_path):
    if file.endswith(".tcx"):
        print(os.path.join(dir_path, file))

fname = raw_input("\nPlease give the tcx filename: ")
actual_dist = float(raw_input("\nPlease give the actual distance: "))
content = open(fname, 'r').read()
distances = re.findall(r"<DistanceMeters>(.*)<\/DistanceMeters>",content,re.MULTILINE)
rec_dist = float(distances[-1])

new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", normalize, content,flags=re.MULTILINE)
new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", "\\g<1>"+str(actual_dist)+"\\g<3>", new_content, 1, flags=re.MULTILINE)

fileToSave = open('EDITED_' + fname, 'w')
fileToSave.write(new_content)
print "File Saved Succesfully."

