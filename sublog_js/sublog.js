var fs = require('fs');
var Showdown = require('showdown');
var converter = new Showdown.converter();
var hljs = require('highlight');
var hl = hljs.Highlight;
var content = fs.readFileSync(process.argv[2], "utf-8");
var html = converter.makeHtml(content);
var output = hl(html, false, true);
console.log(output);
