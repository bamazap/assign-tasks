# assign-tasks

## Usage
`python3 assign_tasks.py example.csv`

## Description
Simple python script to assign tasks to people based on preferences.  

Reads from a CSV file (using commans, not tabs). First column should contain
names of people. First row should contain names of tasks. The cells between them
should be numbers corresponding to each person's desire to do each task
(lower is more desired).  

If some of your tasks need to be assigned to multiple people, simply duplicate
columns.  

Example data is included.  

## Dependencies
- Python 3
- numpy
- scipy
- tabulate
- argparse
