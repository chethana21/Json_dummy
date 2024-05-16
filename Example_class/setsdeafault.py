dict = {'Palestine': ['Ramallah', 'Jerusalem'], 'Kuwait': ['Kuwait City'], 
        'Guinea': ['Conakry'], 'Tokelau': ['Fakaofo'], 'Afghanistan': ['Kabul'], 
        'British Virgin Islands': ['Road Town'], 'Canada': ['Ottawa'],
          'Micronesia': ['Palikir'], 'Panama': ['Panama City']}

x = dict.setdefault('Palestine', 'Ramallah' )
print(x)
y = dict.setdefault('Hong Kong','City of Victoria')
print(y)

print(dict)
