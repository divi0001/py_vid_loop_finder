# py_vid_loop_finder
Using OpenCV python, this programm calculates the top 1000 most similar frames for each frame of a given video and outputs this as a dictionary, written to a json file. The dictionary has the structure of key=current_frame, value = sorted list of top 1000 similar frames
Python file may be executed in CLI, interactive to choose files from a list you can set in the programm, so you can process multiple videos concurrently using multiple CLI instances
