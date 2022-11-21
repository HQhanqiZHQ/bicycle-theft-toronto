
import matplotlib.pyplot as plt
most_most_outer_sizes = [3, 11, 17, 25, 44]
most_outer_sizes = [3, 11, 17, 25, 44]
outer_sizes = [3, 11, 17, 25, 44]
inner_sizes = [3, 11, 17, 25, 44]
most_inner_sizes = [3, 11, 17, 25, 44]
most_most_outer_colors = ['#499894', 'white', 'white', 'white', 'white']
most_outer_colors = ['#499894', '#B07AA1', 'white', 'white', 'white']
outer_colors = ['#499894', '#B07AA1', '#59A14F', 'white', 'white']
inner_colors = ['#499894', '#B07AA1', '#59A14F', '#F28E2B', 'white']
most_inner_colors = ['#499894', '#B07AA1', '#59A14F', '#F28E2B', '#4E79A7']
plt.legend("HOCAT")


plt.pie(most_most_outer_sizes,colors=most_most_outer_colors, startangle=90,frame=True, radius=7)
_, _, autopct = plt.pie(most_inner_sizes,colors=most_inner_colors,radius=6,startangle=90)
                        
plt.pie(most_outer_sizes,colors=most_outer_colors, startangle=90,frame=True, radius=6)
_, _, autopct = plt.pie(most_inner_sizes,colors=most_inner_colors,radius=5,startangle=90,autopct='%1.0f%%',
                        pctdistance=0.5, textprops={'size':15,'color':'white','family':'sarif','style':'italic','backgroundcolor':'black'})
                        
plt.pie(outer_sizes,colors=outer_colors, startangle=90,frame=True, radius=5)
_, _, autopct = plt.pie(most_inner_sizes,colors=most_inner_colors,radius=4,startangle=90)
# for txt, c in zip(autopct, inner_colors):
#     if c == "white":
#         txt.set_visible(False)

plt.pie(inner_sizes,colors=inner_colors, startangle=90,frame=True, radius=4)
_, _, autopct = plt.pie(most_inner_sizes,colors=most_inner_colors,radius=3,startangle=90)


center_circle = plt.Circle((0,0), 1.8, color='black', fc='white', linewidth=0)
plt.gca().add_artist(center_circle)
plt.gcf().set_size_inches(12,12)
plt.axis('equal')
plt.tight_layout()
plt.show()
