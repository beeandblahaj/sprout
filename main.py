import AO3

query = str(input('What would you like to search for? '))
query = '_'.join(query.split(' '))
# Causes an error if query yields too many results in a search.
search = AO3.Search(any_field=query)
search.update()

n = 0
works = []

for result in search.results:
    print(f'{n}: {result.title}')
    works.append(result)
    n = n + 1

workIndex = int(input('Which work would you like to read (number, -1 to turn page)? '))
if (workIndex == -1):
    print('\n')
    while(workIndex == -1):

        search.page = search.page + 1
        search.update()

        for result in search.results:
            print(f'{n}: {result.title}')
            works.append(result)
            n = n + 1

        workIndex = int(input('\nWhich work would you like to read (number, -1 to turn page)? '))
    
try:
    work = works[workIndex]
    work.reload()
    print(work.title)
    f = open(f'{work.title}.html', 'wb')
    f.write(work.download('HTML'))
    
except:

    print('Invalid index/work not found.')
