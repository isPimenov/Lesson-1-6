#словари
my_dict = {'Den':2013, 'Alex':2014, 'Vit':2015, 'Vik':2016}
print('Dict:',my_dict)
print('Existing value:', my_dict['Alex'])
print('Not Existing value:', my_dict.get('Alice', 'такой величины нет'))
my_dict.update({'Alice':2017, 'Olive':2022})
print('Deleted value', my_dict.pop('Vit'))
print('Modified dict', my_dict)
#множества
my_set = {3, 7, 9, 5.5, 3, 8.4, 9,'Grawler','Flanker', True, True}
print(my_set)
my_set.discard('Flanker')
print(my_set)
