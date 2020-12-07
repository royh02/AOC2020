// get input as array
const { fileReader } = require('./fileReader');

// part 1
// ----------------------------------
// fileReader('./puzzle-inputs/day6.txt').then((result) => {
//   let input = result;
//   let curGroup = [];
//   let totalYes = 0;
//   for (let i = 0; i < input.length; i++) {
//     if (input[i] === '') {
//       let ans = new Set(curGroup.join(''));
//       console.log(ans);
//       totalYes += ans.size;
//       curGroup = [];
//     } else {
//       curGroup.push(input[i]);
//     }
//   }
//   console.log(totalYes);
// })
// .catch((err) => {
//   console.error(err);
// });

// part 2
// ----------------------------
fileReader('./puzzle-inputs/day6.txt').then((result) => {
  let input = result;
  let curGroup = [];
  let totalYes = 0;


  for (let i = 0; i < input.length; i++) {
    if (input[i] === '') {
      totalYes += intersection(curGroup).length;
      curGroup = [];
    } else {
      curGroup.push(input[i].split(''));
    }
  }
  console.log(totalYes);
})
  .catch((err) => {
    console.error(err);
  });

// takes in arr of sets
function intersection(arr) {
  return arr.reduce((acc, c) =>
                      acc.filter(i => c.includes(i)))
}