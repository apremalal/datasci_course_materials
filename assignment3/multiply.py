import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mat = record[0]
    i = record[1]
    k = record[2]
    if mat=="a":
      for t in range(0,5):
        mr.emit_intermediate((i,t),record)
    else: 
      for p in range(0,5):
        mr.emit_intermediate((p,k),record)



def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = [0]*5
    b = [0]*5
    for val in list_of_values:
      if val[0] == "a":
        a[val[2]]=val[3]
      else:
        b[val[1]]=val[3]

    tot = 0
    for i in range(0,5):
      tot += a[i]*b[i]
    mr.emit((key[0],key[1],tot))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
