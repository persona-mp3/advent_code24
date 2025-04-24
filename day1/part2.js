const rawDog = require("./rawDataDog.json")
const arr1 = rawDog[0]
const arr2 = rawDog[1]

const calcSimilarityScore = function(arr1, arr2) {
  arr1.sort()
  arr2.sort()

  const {...rest} = iterator(arr2)
  let score = 0

  arr1.forEach(e => {

    if (!rest.set.has(e)) {
      console.log("x")
    } else {
      score += Math.abs(e * rest.store[e])
    }

  })

  return score
}

function iterator(arr2) {
  const set = new Set()
  const doubles = []
  const store = {}

  let i = 0;
  while (i < arr2.length) {

    if (!set.has(arr2[i])) {
      set.add(arr2[i])
      store[arr2[i]] = 1
    } else {
      // doubles.push(arr2[i])
      store[arr2[i]] = ++store[arr2[i]]
    }

    i++
  }

  return {
    store, 
    doubles, 
    set,
  }
}

const s1 = [3, 4, 2, 1, 3, 3]
const s2 = [4, 3, 5, 3, 9, 3]

const score = calcSimilarityScore(arr1, arr2)
console.log("final score is ->", score)
