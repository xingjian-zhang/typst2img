# Makefile for converting SVG to PNG using qlmanage

# Directory containing source (SVG) files
SRC_DIR := output/

# Directory to store output (PNG) files
OUT_DIR := output/

# Get list of SVG files in the SRC_DIR
SVG_FILES := $(wildcard $(SRC_DIR)*.svg)

# Convert SVG filenames to expected PNG filenames in OUT_DIR
PNG_FILES := $(patsubst $(SRC_DIR)%.svg,$(OUT_DIR)%.png,$(SVG_FILES))

# Default target: convert all SVGs to PNGs
all: $(PNG_FILES)

# Rule to convert an SVG file to PNG using qlmanage
$(OUT_DIR)%.png: $(SRC_DIR)%.svg
	convert -density 1000 $< $@

# Phony target to prevent make from getting confused by actual files named "clean"
.PHONY: clean

# Clean up output directory
clean:
	rm -f $(PNG_FILES)
