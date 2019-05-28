import pygal
from pygal.style import TurquoiseStyle as TS, LightenStyle as LS

from question import Question

file_list = ['data/rff_q1.csv', 'data/rff_q2.csv', 'data/rff_q3.csv',
             'data/rff_q4.csv', 'data/rff_q5.csv', 'data/rff_q6.csv',
             'data/rff_q7.csv']

questions = [Question(file) for file in file_list]

# Make Visualization
chart_style = LS('#F3E500', base_style=TS)
chart_style.title_font_size = 20
for question in questions:
    chart = pygal.HorizontalBar(style=TS, rounded_bars=5, show_legend=False)
    chart.title = question.question_text
    chart.x_labels = question.labels
    chart.add('', question.plot_dicts)
    chart.render_to_file('charts/' + question.svg_name)