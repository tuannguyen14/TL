var json = require('./save_file.json')
json = json['users']

json.forEach(element => {
    console.log(element['email'])
});