import os
import re
max_speed = 0

def normalize(match):
	global max_speed
	dist = float(match.group(2))
	spd = float(match.group(4))
	new_dist = dist*actual_dist/rec_dist
	new_spd = spd*new_dist/dist
	if new_spd > max_speed: max_speed = new_spd
	return match.group(1) + str(new_dist) + match.group(3) + str(new_spd) + match.group(5)

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

# new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", normalize, content,flags=re.MULTILINE)
toMatch = r"""(<Trackpoint>
            <Time>.*</Time>
            <DistanceMeters>)(.*)(</DistanceMeters>
            <Extensions>
              <ns3:TPX>
                <ns3:Speed>)(.*)(</ns3:Speed>
              </ns3:TPX>
            </Extensions>
          </Trackpoint>)"""
new_content = re.sub(toMatch, normalize, content,flags=re.MULTILINE) # Fix Distances and speeds
new_content = re.sub(r"(<DistanceMeters>)(.*)(<\/DistanceMeters>)", "\\g<1>"+str(actual_dist)+"\\g<3>", new_content, 1, flags=re.MULTILINE) # Fix Total Distance
new_content = re.sub(r"(<MaximumSpeed>)(.*)(<\/MaximumSpeed>)", "\\g<1>"+str(max_speed)+"\\g<3>", new_content, 1, flags=re.MULTILINE) # Fix Max Speed

fileToSave = open('EDITED_' + fname, 'w')
fileToSave.write(new_content)
print "File Saved Succesfully."

