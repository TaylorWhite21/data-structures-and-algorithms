def loop_reverse(string):
  empty_string = ''
  for i in string:
    empty_string = i + empty_string
  return empty_string
  
string = 'Reinhardt'
print(string)
print(f'reversed: {loop_reverse(string)}')

def slice_reverse(string):
  return string[::-1]

string = 'Reinhardt'
print(string)
print(f'slice reversed: {slice_reverse(string)}')

reversed_string=''.join(reversed(string))
print(f'slice reversed: {reversed_string}')
