
def make_unique(positive, negative):
   print('starting unique')
   for p in positive:
      if p in negative:
         positive.remove(p)
   print('halfway through')
   for n in negative:
      if n in positive:
         negative.remove(n)
   print('in unique')
