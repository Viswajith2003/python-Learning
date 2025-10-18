//Using array

// let arr = [2, 3, 5, 4, 3, 1, 2];
// let res=[]

// function Dupli(arr) {
//   for (let i = 0; i <= arr.length; i++) {
//     for (let j = i + 1; j <= arr.length; j++) {
//       if (arr[i] === arr[j] && !res.includes(arr[i])) {
//         res.push(arr[i])
//       }
//     }
//   }
//   return res;
// }

// console.log(Dupli(arr));

//Using set

let arr = [2, 3, 5, 4, 3, 1, 2];
let current = new Set();
let dupli = new Set();

for (let num of arr) {
  if (current.has(num)) {
    dupli.add(num);
  } else {
    current.add(num);
  }
}

console.log([...dupli]);
