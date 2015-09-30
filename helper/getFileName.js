var inputFilePath  = process.argv[2];
var inputFileName  = inputFilePath.split('/');
inputFileName = inputFileName[inputFileName.length - 1].split('.')[0];

console.log(inputFileName);
