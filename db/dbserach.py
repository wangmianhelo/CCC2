import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['tweets']
result = db.view('my_design/name1')
list = []
print(result)
for row in result:
  data = row.value
  list.append({data['city']:data['income']})

print(list)