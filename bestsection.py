import pandas as pd
df = pd.read_csv('C:\\Users\\KIIT\\Desktop\\Code\\Python\\Notebooks\\Time Table File.csv')

# df = pd.read_excel('C:\\Users\\KIIT\\Desktop\\Code\\Python\\Notebooks\\Time Table File.xls')

newdf = df.loc[df['Section'].str.contains('CSE', na = False)]
new_df = newdf.loc[(df['4-5'] == 'X') & (df['5-6'] == 'X')]

new_df.to_excel('C:\\Users\\KIIT\\Desktop\\Code\\Python\\Notebooks\\timetablenew.xlsx', index = 0)
# print(new_df.head(100))

section_list = []
only_section_list = []
for section in (new_df['Section']): 
    section_list.append(section)
    if section_list.count(section) >= 2: 
        continue
    else: 
        only_section_list.append(section)
    
section_list.sort()
only_section_list.sort()
print(section_list.count('CSE-24'))
for section in only_section_list:
    if section_list.count(section) == 6: 
        print(section)

# for cls in section_list: 
#     new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]


