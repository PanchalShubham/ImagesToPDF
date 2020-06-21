#!/usr/bin/env python3

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


# define the process_directory procedure
def process_directory(image_directory, output_path):
	"""Takes a directory path and output file path and writes images as pdf to file"""
	# check if directory exist
	if not os.path.isdir(image_directory):
		print("{} doesn't exist".format(image_directory))
	# check if file ends with pdf
	elif not output_path.endswith(".pdf"):
		print("{} doesn't represent a path to a pdf file".format(output_path))
	# check if output file already exist
	elif os.path.isfile(output_path):
		print("{} already exist".format(output_path))
		# prompt user wheter to overwrite data
		choice = input("Do you want to overwrite data(yes/no)? ")
		# take decision based on user's choice
		if choice.lower() != "yes":
			# user opted for not to overwrite the data
			print("Overwriting aborted by user")
			# return since user aborted the process
			return

	# give a simple message to user
	print("Working on your request...")
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
		# create an instance of FPDF
		pdf = FPDF(unit="pt", format=[max_width + 2*margin, max_height + 2*margin])
		# for each image add it to pdf
		for imagePath in image_path_list:
			# add a new page to pdf
			pdf.add_page()
			# add image to pdf
			pdf.image(imagePath, margin, margin)
		# write the pdf to system
		pdf.output(output_path, "F")
		# give a message to user
		print("Request completed!")
	except Exception:
		# give an error message to user
		print("Oops, something went wrong ):")

# define main function - works with command line argumsnt
def main():
	"""Accepts the source directory containing images and output pdf path and 
		converts images into a pdf sorted by name"""
	if len(sys.argv) != 3:
		print("Usage:")
		print("python3 source_dir output_pdf_path")
		print("or")
		print("./img2pdf source_dir output_pdf_path")
	else:
		process_directory(sys.argv[1], sys.argv[2])

# call the main procedure to start the script
main()
