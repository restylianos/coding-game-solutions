const N = parseInt(readline());

const sortArr = (arr) => arr.sort((a, b) => a - b);
const numbers = []

for (let i = 0; i < N; i++) {
    const pi = parseInt(readline());
    numbers.push(pi);
}

let dif;
const res = sortArr(numbers);

for (let i = 1; i < res.length; i++) {
    const numDif = Math.abs(res[i] - res[i - 1]);
    if (i === 1) {
        dif = numDif;
        continue;
    }
    if (dif > numDif) dif = numDif;
}
console.log(dif)
