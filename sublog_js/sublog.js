var fs = require('fs');
var Showdown = require('showdown');
var converter = new Showdown.converter();
var hljs = require('highlight');
var hl = hljs.Highlight;
var content = fs.readFileSync(process.argv[2], "utf-8");
var html = converter.makeHtml(content);
var showLn = process.argv[3] === 'true'
var output = hl(html, false, true, showLn);
console.log(output);
