import os
import re

def normalize(match):
	dist = match.group(2)
	dist = float(dist) * actual_dist/rec_dist
	return match.group(1) + str(dist) + match.group(3)
print
print
print "1.    D i s t a n c e    N o r m a l i z e r"
print
print "(For any request/help email me @ \"georgiou.kostas@hotmail.com\")"
print
dir_path = os.path.dirname(os.path.realpath(__file__))
tcx_inputs = dir_path+"/Inputs/TCX/"
tcx_outputs = dir_path+"/Outputs/TCX/"
print "\nList of available tcx files in the Inputs/TCX Directory:"
for file in os.listdir(tcx_inputs):
    if file.endswith(".tcx"):
        print(os.path.join(tcx_inputs, file))

fname = raw_input("\nPlease give the tcx filename: ")
actual_dist = float(raw_input("\nPlease give the activity\'s correct distance: "))
content = open(tcx_inputs+fname, 'r').read()

distances = re.findall(r"<DistanceMeters>(.*)<\/DistanceMeters>",content,re.MULTILINE)
rec_dist = float(distances[-1])

new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", normalize, content,flags=re.MULTILINE)
new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", "\\g<1>"+str(actual_dist)+"\\g<3>", new_content, 1, flags=re.MULTILINE)

fileToSave = open(tcx_outputs+'EDITED_' + fname, 'w')
fileToSave.write(new_content)
print
print "File Saved Succesfully."
print
print "Now go to http://www.gpxeditor.co.uk/ and draw your route until the distances it shows matches your actual distance."
print "Then export the gpx file, place it in \"Inputs/GPX\" and run 2_addTimespampsFromTCXtoGPX.exe"

