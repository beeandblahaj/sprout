import AO3

query = str(input('What community would you like to search for? '))
search = AO3.Search(fandoms=query)
search.update()
n = 0
works = []

for result in search.results:
    print(f'{n}: {result.title}')
    works.append(result)
    n = n + 1

workIndex = int(input('Which work would you like to read (number, -1 to turn page)? '))
if (workIndex == -1):
    while(workIndex == -1):
        search.page = search.page + 1
        search.update()
        for result in search.results:
            print(f'{n}: {result.title}')
            works.append(result)
            n = n + 1
        workIndex = int(input('Which work would you like to read (number, -1 to turn page)? '))
    
elif (workIndex > -1 and works[workIndex]):
    work = works[workIndex]
    work.reload()
    print(work.title)
    f = open(f'{work.title}.html', 'wb')
    f.write(work.download('HTML'))
    
else:
    print('No work found/Invalid index')
