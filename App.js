const {readFile, writeFile} = require('fs');


readFile('./tmp.txt','utf8', (err, res) => {
    if(err){
        console.log("ERROR: ",err)
        return
    }
    console.log(res);
}) 