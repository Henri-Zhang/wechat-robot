# -*- coding: UTF-8 -*-

import itchat
import pygal
from pygal import Config
from pygal.style import LightColorizedStyle

itchat.auto_login()

counts = {
  'Male': 0,
  'Female': 0,
  'Unknown': 0
}
friends = itchat.get_friends(update=True)[0:]

for friend in friends:
  if(friend['Sex'] == 0):
    counts['Unknown'] += 1
  elif(friend['Sex'] == 1):
    counts['Male'] += 1
  elif(friend['Sex'] == 2):
    counts['Female'] += 1

print(counts)

config = Config()
config.show_legend = False
config.human_readable = True
config.print_values=True
config.style = LightColorizedStyle

pie_chart = pygal.Bar(config)
pie_chart.title = 'Gender histogram of Wechat friends'
pie_chart.x_labels = ['Male', 'Female', 'Unknown']

pie_chart.add('', [
  {
    'value': counts['Male'],
    'style': 'fill: blue; stroke: black; stroke-width: 2'
  },
  {
    'value': counts['Female'],
    'style': 'fill: red; stroke: black; stroke-width: 2'
  },
  {
    'value': counts['Unknown'],
    'style': 'fill: gray; stroke: black; stroke-width: 2'
  }
])

pie_chart.render_to_png('gender_histogram.png')