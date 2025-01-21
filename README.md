# os-threading
In this lab, you will implement a threaded program in Python. You may work with a partner on this lab.
## Set Up
This lab requires an experimental version of Python, so follow the set up instructions carefully.
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create -n os-threading --override-channels -c conda-forge python-freethreading</li>
		<li>conda activate os-threading</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the os-threading anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
  You will be using threads to download csv files from urls and write the data to csv files. 
  <li>Template</li>
  <ul>
    <li>The template includes a list of urls and a list of filenames for you to use in this lab.</li>
  </ul>
  <li>download_files(url, filename, thread)</li>
  <ul><li>this funciton takes in the url to the data, the filename of the output file, and the thread number. This function will download and write the data to the output csv file. This function should also output the following messages when the function begins and ends:<br>
  Thread 1 starting<br>
  Thread 2 starting<br>
  Thread 3 starting<br>
  Thread 4 starting<br>
  Thread 5 starting<br>
  .<br>
  .<br>
  .<br>
  Thread 2: AirQualityData.csv downloaded in 1.87 seconds<br>
  Thread 5: MeteoriteLandings.csv downloaded in 1.93 seconds<br>
  Thread 1: ElectricVehicleData.csv downloaded in 13.84 seconds<br>
  Thread 3: WalkabilityIndex.csv downloaded in 34.44 seconds
  </li>
  </ul>
<li>Threads</li>
  <ul>
    <li>Create 5 threads using the Python threading module that will call the download_files function and pass the appropriate arguments to the function.</li>
    <li>Thread 1 should handle the first url and write to the first filename. Thread 2 should handle the second url and write the the second file name. etc</li>
    <li>Do not use a for loop</li>
    <li>You may experiment with other files but submit your code with url and filename list included with the template.</li>
  </ul>
</ol>

## Modules
You will probably need to import requests, threading, and time modules to successfully complete this lab. 
