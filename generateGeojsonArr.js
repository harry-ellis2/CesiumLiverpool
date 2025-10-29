const fs = require('fs');
const files = fs.readdirSync('resources');
const geojsonUrls = files.map(f => 'resources/' + f);
console.log(JSON.stringify(geojsonUrls, null, 2));