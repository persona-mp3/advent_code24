const rawDog = require("./rawDataDog.json")
const arr1 = rawDog[0]
const arr2 = rawDog[1]
console.log(arr1.length, arr2.length)


const totalDays = function (arr1, arr2) {
  arr1.sort()
  arr2.sort()

  let totalDays = 0
  for (let i=0; i < arr1.length; i++) {
    totalDays += Math.abs(arr1[i] - arr2[i])
  }

  return totalDays
}

const result = totalDays(arr1, arr2)
console.log(result)
