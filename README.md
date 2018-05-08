# Garmin Activity - Distance Normalizer

Garmin Vivofit 3 does not track correctly swimming distances and doesn't have gps. 

With this app you can fix these distances and add geolocation to your activity.

Steps:


1. Export your swimming activity's tcx file from garmin connect.

2. Place in "Inputs/TCX".

3. Run activity_distance_normalizer.py select the exported file and type the actual distance you swam.

(If you don't want geolocation skip steps 4-10)

4. Go to http://www.gpxeditor.co.uk/ and draw your swimming route until the distances it shows matches your actual distance.

5. Export the gpx file and place it in "Inputs/GPX".

6. Run activity_addTimespampsFromTCX.py and select the tcx file you created in step 2 and the gpx file you exported in step 5.

7. Download GpxTcxWelder from https://sourceforge.net/projects/gpxtcxwelder/ and install it.

8. Run it and select the tcx and the gpx files from "Outputs/TCX" and "Outputs/GPX".

9. Click start processing and click Save (save it as a tcx file).

10. Open the saved tcx file and replace all the lines before the "<Activities>" with the corresponding lines for your first initial file.

11. Your activity is now ready to be imported to any activity tracking website (such as Strava and Garmin Connect) !


I know it's frustrating having to do all this steps, so I will try to automate most of the processes in the future.