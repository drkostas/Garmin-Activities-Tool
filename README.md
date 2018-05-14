# Garmin Activity Tool

Garmin Vivofit 3 does not track correctly swimming distances and doesn't have gps. 

With this app you can fix the distances and add geolocation to any activity.

Steps:


1. Export your activity's tcx file from garmin connectc and place it in "Inputs/TCX".

2. Run 1_distanceNormalizer.exe, select the exported file and type the correct distance you crossed.

   (If you don't want geolocation your are done!)

3. Go to http://www.gpxeditor.co.uk/ and draw your route (make sure that the distance it shows matches your actual distance).

   - Export the gpx file and place it in "Inputs/GPX".

4. Run 2_addTimespampsFromTCXtoGPX.exe, select the tcx file you created in step 3 and the gpx file you exported in step 5.

5. Download GpxTcxWelder from https://sourceforge.net/projects/gpxtcxwelder/ and install it.

   - Run it and select the tcx and the gpx files from "Outputs/TCX" and "Outputs/GPX".

   - Click start processing, click Save and place the new tcx file in Inputs/GpxTcxWelder

6. Run 3_cleanHeader.exe, select your original tcx file and the one you saved from GpxTcxWelder.

Congratulations!!

Your final activity is ready inside Outputs/GpxTcxWelder. You can now import it an any activity tracking website (such as Strava and Garmin Connect)!

For any request/help email me @ georgiou.kostas@hotmail.com

(I'm in the process of reducing the required steps.)