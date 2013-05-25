import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    id = record[1]
    mr.emit_intermediate(id,record)

def reducer(key, list):
    # key: record id
    order = []
    for v in list:      
      if v[0] == 'order':
        order = v
        break

    
    for item in list:
      ele =[]
      del ele[:]
      ele[:] = order 
      if item[0] != 'order':
        ele.extend(item) 
        mr.emit(ele)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
