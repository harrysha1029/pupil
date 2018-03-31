''' Parameters for the pipeline'''

params = {}

# Outputs of the pipeline will contain this as a substring
# Use '' to have it be set automatically
params['base_name'] = ''

# Outputs of the pipeline will contain this as a substring
# Use '' to have it be set automatically
params['out_dir'] = ''

# True if you want to select the files with a GUI
params['choose_files'] = False

# List of paths for pupil_data relative to the main folder
# Note: only effective if choose_files is False
params['eye_paths'] = ['/home/harrysha/Dropbox/data/S18_120/Run2/S18_120-pupil_data-run2.xlsx']

# Same as eye_paths for the events files
params['events_paths'] = ['/home/harrysha/Dropbox/data/S18_120/Run2/events.mat']

# Filter samples greater than this value (mm)
params['impossible_upper'] = 5

# Filter samples below this value (mm)
params['impossible_lower'] = 1.5

# Sections with zeros that are below this threshold will be interpolated (ms)
params['max_blink_time'] = 500

# Sections with zeros that are below this threshold will be front filled(ms)
params['min_blink_time'] = 20

# In hertz
params['sample_rate'] = 250

# 'no' for no baseline
# an integer, x, to use the average value of x seconds before event as baseline
# a tuple('cond', a, duration) to use the value from the previous event of the condition at
# index a. Takes the average duration seconds after the event.
params['baseline_type'] = ('cond', 0, 900)

# Number of milliseconds to epoch after trial onset (ms)
params['epoch_time'] = 2500

# Number of milliseconds prior to epoch to show
# Multiple of 4 please :)
params['back_time'] = 200

# List of conditions to be plotted, or 'all' for all conditions
params['conds_to_plot'] = [1, 2, 3]

# List of colors (in hex) to plot. NOTE you need to change this
# if you're plotting more than 10 conditions.
params['plot_colors'] = ['#e218d8', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Style of each line to plot. See:
# https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
params['plot_style'] = ['-' for i in range(10)]

# True to plot error bars (SE) and False for no error bars.
params['plot_error'] = True

# Title of the plot
params['plot_title'] = 'Pupil Diameter'

# Y axis label
params['y_label'] = 'Pupil diameter (mm)'

# File name of the plot
params['plot_fname'] = 'pupil_diameter_plot'
