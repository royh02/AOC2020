const { once } = require('events');
const { createReadStream } = require('fs');
const { createInterface } = require('readline');

async function fileReader(location) {
  try {
    const rl = createInterface({
      input: createReadStream(location),
      crlfDelay: Infinity
    });
    let arr = [];
    rl.on('line', line => {
      arr.push(line.trim())
    });

    await once(rl, 'close');
    return arr;
  } catch (err) {
    console.error(err);
  }
};


module.exports = { fileReader };