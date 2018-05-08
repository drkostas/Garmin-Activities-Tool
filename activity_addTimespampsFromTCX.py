import os
import re

step = 0
def transfer_times(match):
	global step
	global offset
	while step+1 > len(tcx_times):
		step-=1
	trkpt = match.group(1) + "><time>" + tcx_times[int(round(step))] + "</time></trkpt>"
	step += offset
	return trkpt

dir_path = os.path.dirname(os.path.realpath(__file__))
tcx_outputs = dir_path+"/Outputs/TCX/"
gpx_inputs = dir_path+"/Inputs/GPX/"
gpx_outputs = dir_path+"/Outputs/GPX/"
print "\nList of all tcx files in the outputs Directory:"
for file in os.listdir(tcx_outputs):
    if file.endswith(".tcx"):
        print(os.path.join(tcx_outputs, file))

tcxname = raw_input("\nPlease give the tcx filename: ")

print "\nList of all gpx files in the Inputs Directory:"
for file in os.listdir(gpx_inputs):
    if file.endswith(".gpx"):
        print(os.path.join(gpx_inputs, file))

gpxname = raw_input("\nPlease give the gpx filename: ")

tcx_content = open(tcx_outputs+tcxname, 'r').read()
gpx_content = open(gpx_inputs+gpxname, 'r').read()

tcx_times = re.findall(r"<Time>(.*)<\/Time>",tcx_content,re.MULTILINE)
tcx_count = float(len(tcx_times))
gpx_count = float(len(re.findall(r"<trkpt",gpx_content,re.MULTILINE)))
print "tcx count: ", tcx_count
print "gpx count: ", gpx_count
offset = tcx_count/gpx_count
print "Offset: ", offset

new_gpx_content = re.sub(r"(<trkpt lat=\".*\" lon=\".*\") />", transfer_times, gpx_content,flags=re.MULTILINE)

fileToSave = open(gpx_outputs+'EDITED_' + gpxname, 'w')
fileToSave.write(new_gpx_content)
print "File Saved Succesfully."

