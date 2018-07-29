import matplotlib.pyplot as plt
import yaml

f = plt.figure()

#Read Config
with open('vars.yaml', 'r') as fi:
    vars = yaml.load(fi)

#Read data into app

for line in vars['lines']:
    xLines = [vars['graph']['x'][0]]
    yLines = [vars['graph']['y'][0]]

    yholder = vars['graph']['y'][0]
    xholder = 0
    for point in line['data']:
        xLines.append(point[1])
        xLines.append(point[1])
        yLines.append(yholder)
        yLines.append(point[0])
        yholder = point[0]
        xholder = point[1]
    xLines.append(vars['graph']['x'][1])
    yLines.append(yholder)
    plt.plot(xLines, yLines)


#Make the graph
plt.axis([vars['graph']['x'][0], vars['graph']['x'][1], vars['graph']['y'][0], vars['graph']['y'][1]])
plt.xlabel(vars['graph']['xLabel'])
plt.ylabel(vars['graph']['yLabel'])
plt.title(vars['graph']['title'])
# plt.annotate('No Trip Zone', xy=(vars['graph']['noTripXY'][1], vars['graph']['noTripXY'][0]), xytext=(3, 1.5))
plt.grid(True)
plt.show()

#Make the outfile
#out = input('Name and extension of file: (ex: file.pdf)')
#f.savefig(out, bbox_inches='tight')