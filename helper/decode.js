var fs = require('fs');

var inputFilePath  = process.argv[2];
var inputFileName  = inputFilePath.split('/');
inputFileName = inputFileName[inputFileName.length - 1];
var outputFilePath = 'char/' + inputFileName;

var contents = fs.readFileSync(inputFilePath);
var lines = contents.toString().split('\n');

var str = '';
lines.forEach(function (line) {
    var decoded = decodeURIComponent(line);
    str = str + decoded + '\n';
});

var body = str.substring(0, str.length - 1);
fs.writeFileSync(outputFilePath, body, 'utf8');

console.log('Decoded.');
