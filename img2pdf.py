# author: Shubham Panchal(http://shubhampanchal.herokuapp.com)
# This small python script converts a set of images into a pdf file
# arranging images in lexicographical-order of names
# you can edit/modify this script as per your needs
# make a not on extension list supported (update it if you need)
# dependencies:
# pip3 install fpdf


#import necessary python modules
from fpdf import FPDF
from PIL import Image
import os
import sys
import glob
import threading

# prints the progress report to console
def print_progress_report(percentage):
	"""Prints the report to console"""
	# print the work-done in percentage
	print("\rProgress: [", end='')
	# print percentage many #'s
	for i in range(percentage):
		print("#", end='')
	# print (100 - percentage) many -'s
	for i in range(100 - percentage):
		print('-', end='')
	# print the closing bracker
	print("] {}%".format(percentage), end='')


# generates a pdf in background thread
def generate_pdf(image_path_list, output_path):
	try:
		# get the max width and max height
		max_width = 0
		max_height = 0
		# iterate through all images
		for imagePath in image_path_list:
			# get the image
			image = Image.open(imagePath)
			# get the size of the image
			width,height = image.size
			# update max_width
			max_width = max(max_width, width)
			# update max_height
			max_height = max(max_height, height)
		# margin of 10pt
		margin = 10
		# get the number of images to process
		total = len(image_path_list)
		# get the number of images processed
		processed = 0
		# print the zero-progress report
		print_progress_report(0)
		# create an instance of FPDF
		pdf = FPDF(unit="pt", format=[max_width + 2*margin, max_height + 2*margin])
		# for each image add it to pdf
		for imagePath in image_path_list:
			# compute the percentage of work done
			percentage = int(100*processed/total) 
			# print the progress report
			print_progress_report(percentage)
			# add a new page to pdf
			pdf.add_page()
			# add image to pdf
			pdf.image(imagePath, margin, margin)
			# increase the number of images processed by 1
			processed += 1
		# write the pdf to system
		pdf.output(output_path, "F")
		# print the percentage of total work-done
		print_progress_report(100)
		# leave a simple next line
		print('')
		# give a simple message to user
		print("Request completed!")
	# catch exception (if any)
	except Exception:
		print("\nOops, something went wrong )-:")


# define the process_directory procedure
def process_directory(image_directory, output_path):
	"""Takes a directory path and output file path and writes images as pdf to file"""
	# check if directory exist
	if not os.path.isdir(image_directory):
		# give a message to user
		print("{} doesn't exist".format(image_directory))
		# return from process
		return
	# check if file ends with pdf
	elif not output_path.endswith(".pdf"):
		# give a message to user
		print("{} doesn't represent a path to a pdf file".format(output_path))
		# return from the process
		return
	# check if output file already exist
	elif os.path.isfile(output_path):
		# give a message to user
		print("{} already exist".format(output_path))
		# prompt user wheter to overwrite data
		choice = input("Do you want to overwrite data(yes/no)? ")
		# take decision based on user's choice
		if choice.lower() != "yes":
			# user opted for not to overwrite the data
			print("Overwriting aborted by user")
			# return since user aborted the process
			return


	# get the directory of the output_path
	output_dir = os.path.dirname(os.path.realpath(output_path))
	# check if this represents a valid directory on os
	if not os.path.isdir(output_dir):
		# give a message to user
		print("{} doesn't exist".format(output_dir))
		# return from the process
		return


	# give a simple message to user
	print("Collecting files image files in {}".format(image_directory))
	try:
		# add extensions here
		extensions = ('*.jpg','*.png','*.gif')
		# store the list of image-path
		image_path_list = []
		# fetch all image with given extension from user's directory
		for extension in extensions:
			image_path_list.extend(glob.glob(os.path.join(image_directory, extension)))
		# sort the files w.r.t file names
		image_path_list.sort()
		# check if there exist some-file
		if len(image_path_list) == 0:
			# give a message to user
			print("Sorry, we couldn't find any file in {} for generating a pdf!".format(image_directory))
			# return from this point
			return
		# give user a message
		print("Following files are going to be compressed to a pdf in same order:")
		# print list to console
		print(image_path_list)
		# prompt user
		choice = input("Are you sure to continue(yes/no)? ")
		# take decision based on user's choice
		if choice.lower() != "yes":
			# user opted for not to overwrite the data
			print("Process aborted by user")
			# return since user aborted the process
			return
		# writing to pdf
		print("Generating {}...".format(output_path))
		# create a thread to run process
		thread1  = threading.Thread(target=generate_pdf, args=(image_path_list, output_path,))
		# set the daemon for thread1 to true
		thread1.daemon = True
		# start thread-1
		thread1.start()
		# wait until thread1 is finished
		thread1.join()
	except Exception:
		# give an error message to user
		print("\nOops, something went wrong ):")


# shows the usage of script to user
def show_usage():
	print("Usage:")
	print("To generate a pdf `output_pdf_path` from images in `source_dir` use the following command:")
	print("python3 img2pdf.py source_dir output_pdf_path")
	print("Dependencies: pip3 install fpdf")

# define main function - works with command line argumsnt
def main():
	"""Accepts the source directory containing images and output pdf path and 
		converts images into a pdf sorted by name"""
	if len(sys.argv) != 3:
		# show usage to user
		show_usage()
	else:
		process_directory(sys.argv[1], sys.argv[2])

# call the main procedure to start the script
main()
