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
print "\nList of all tcx files in this Directory:"
for file in os.listdir(dir_path):
    if file.endswith(".tcx"):
        print(os.path.join(dir_path, file))

tcxname = raw_input("\nPlease give the tcx filename: ")

print "\nList of all gpx files in this Directory:"
for file in os.listdir(dir_path):
    if file.endswith(".gpx"):
        print(os.path.join(dir_path, file))

gpxname = raw_input("\nPlease give the tcx filename: ")

tcx_content = open(tcxname, 'r').read()
gpx_content = open(gpxname, 'r').read()

tcx_times = re.findall(r"<Time>(.*)<\/Time>",tcx_content,re.MULTILINE)
tcx_count = float(len(tcx_times))
gpx_count = float(len(re.findall(r"<trkpt",gpx_content,re.MULTILINE)))
print "tcx count: ", tcx_count
print "gpx count: ", gpx_count
offset = tcx_count/gpx_count
print "Offset: ", offset

new_gpx_content = re.sub(r"(<trkpt lat=\".*\" lon=\".*\") />", transfer_times, gpx_content,flags=re.MULTILINE)

fileToSave = open('EDITED_' + gpxname, 'w')
fileToSave.write(new_gpx_content)
print "File Saved Succesfully."

