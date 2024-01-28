const {spawn, fork, spawnSync} = require('child_process');


function buildPseudoTree() {
        const python = spawn('python',['id3.py'], { slient:true,
        detached:true,
          stdio: [null, null, null, 'ipc']});
   
        console.log("waiting");
        python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
       
       });
   
    
    
    
    //return "executing";
}
buildPseudoTree();

module.exports = {buildPseudoTree}