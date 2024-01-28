const express = require('express');
const {spawn, fork, spawnSync} = require('child_process');
const fileUpload = require('express-fileupload');
const fs = require('fs');
const cors = require('cors');
const timeout = require('connect-timeout');
const { setTimeout } = require('timers/promises');
const app = express();
app.use(express.json());
app.use(cors());
app.use(fileUpload())
app.use(timeout('500s'));
//let newProcessDescriptor = spawn('../node_modules/',{ detached: true })
app.post('/', (req, res)=> {
    console.log(req.files)
    const fileName = req.files.MyFile.name;
    const file = req.files.MyFile;
    let extension = req.files.MyFile.name.split('.');
    extension = extension[1];
    if( extension != 'csv' ) {
        res.status(400).json({
            'message': 'Favor de cargar un archivo con extensión csv'
        });
    }else {
        let uploadPath = __dirname +'/uploads/myDataSet.csv';
        file.mv(uploadPath, (err) => {
            if(err){
                return res.send(err);
            }
        })
        res.status(200).json({
            'extension':extension,
            'name': fileName,
            'Message': 'Archivo cargado correctamente'
        });
    }
    
});


//validate if the system has a file in the database
app.get('/validateFile', (req, res) => {
    var response = false;
    const arrayOfFiles = getFiles('uploads')
    const found = arrayOfFiles.find( (element) => element == 'uploads/myDataSet.csv' );
    if(found == 'uploads/myDataSet.csv') { 
        response = true;
    }else{
        response = false;
    }
    res.status(200).json({
        response
    });
});


//Execute a python file
app.get('/firstProcess',  (req, res) => {
    //validate if pseudoTree file is filled up
    let out = fs.openSync('./out.log', 'a');
    let err = fs.openSync('./out.log', 'a');
    fs.writeFile('pseudoTree.txt', '', function(){console.log('done')});


    //await cmd(res);
    const python = fork('child.js', {
        detached: true,
        stdio: 'ignore'
      });
    python.send('start');
    python.unref();
    python.disconnect(); 
    
    res.setTimeout(1000, function(){
        //clearInterval(interval);
        console.log('Request has timed out.');
        res.status(500).send('Response Processing Timed Out.');
        
    });
    //python.send('start');
    /*python.on('message', data => {
        res.send("hola");
    })*/
    //python.unref();
    
    /*python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
       });
       //res.send("okas")
        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            // send data to browser
            
            res.send("Proceso completado");
        });
        */
});


function cmd(res) {
    let p = spawn('python',['id3.py'], { detached: true });
    return new Promise((resolveFunc) => {
      p.stdout.on("data", (x) => {
        console.log("no error");
        res.send("No error");
      });
      p.stderr.on("data", (x) => {
        res.send("error");
        console.log("error")
      });
      p.on("exit", (code) => {
        resolveFunc(code);
        res.send("Resolved");
      });
    });
  }
  


app.get('/secondProcess', (req,res) => {
    //validate if pseudoTree file is filled up
    fs.writeFile('processedPseudoTree.txt', '', function(){console.log('done')});



    const python = spawn('python',['secondProcess.py']);
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
       });
        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            // send data to browser
            res.send("Proceso completado");
        });
});

app.get('/createTree', (req,res) => {
  //validate if pseudoTree file is filled up
  fs.writeFile('treeJsonFormat.json', '', function(){console.log('done')});



  const python = spawn('python',['tree.py']);
  python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...');
      dataToSend = data.toString();
     });
      python.on('close', (code) => {
          console.log(`child process close all stdio with code ${code}`);
          // send data to browser
          res.send("Proceso completado");
      });
});


app.get('/sendTree', (req, res) => {
  fs.readFile("./treeJsonFormat.json", "utf8", (error, data) => {
    if (error) {
      //console.log(error);
      return;
    }
    //console.log(JSON.parse(data));
    res.status(200).json({
      "tree": [JSON.parse(data)]
    });
  });
});


app.get('/sendOptions', (req, res) => {
  fs.readFile("./frontOptions.json", "utf8", (error, data) => {
    if (error) {
      //console.log(error);
      return;
    }
    //console.log(JSON.parse(data));
    //data.options[0].pop();
    res.status(200).json({
      "options": JSON.parse(data)
    });
  });
})

app.listen(4000);



// Recursive function to get files
function getFiles(dir, files = []) {
    // Get an array of all files and directories in the passed directory using fs.readdirSync
    const fileList = fs.readdirSync(dir)
    // Create the full path of the file/directory by concatenating the passed directory and file/directory name
    for (const file of fileList) {
      const name = `${dir}/${file}`
      // Check if the current file/directory is a directory using fs.statSync
      if (fs.statSync(name).isDirectory()) {
        // If it is a directory, recursively call the getFiles function with the directory path and the files array
        getFiles(name, files)
      } else {
        // If it is a file, push the full path to the files array
        files.push(name)
      }
    }
    return files
  }

