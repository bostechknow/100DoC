const path = require("path")
const util = require("util")
const fs = require("fs")

const readdir = util.promisify(fs.readdir);

const config = {
    typeDirs: [
        { type: ".pdf", directory: "documents" },
        { type: ".png", directory: "images" },
        { type: ".mp3", directory: "music" }
    ]
}

const directory = process.argv[2]

if(!directory){
    console.log("Specify the target directory")
    return;
}

[...config.typeDirs, { directory: "other" } ].map( d => {
    const dirname = `${directory}/${d.directory}`;
    if(!fs.existsSync(dirname)){
        fs.mkdirSync(dirname)
    }
});

( async () => {
    const files = await readdir(directory)

    files.forEach(file => {
        const extname = path.extname(file)
        if(!extname) {
            return
        }

        const { directory: targetDir = "other" } = config.typeDirs.find(dir => dir.type == extname) || {};

        const oldPath = path.join(__dirname, directory, file)
        const newPath = path.join(__dirname, directory, targetDir, file)

        fs.rename(oldPath, newPath, function(err) {
            if(err){
                throw err
            }
        });
    });
})();

// console.log("Hello World!")
// Learn NodeJS in 10 minutes - How to install correctly and make a file management app by Maksim Ivanov
// https://www.youtube.com/watch?v=elBNFO8nsaw
// IIAAF https://2ality.com/2016/10/async-function-tips.html#immediately-invoked-async-function-expressions

