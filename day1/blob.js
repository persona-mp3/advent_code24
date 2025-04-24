const data = document.querySelector("pre").innerText

const arr1 = []
const arr2 = []

data.split("\n").forEach((line) => {
  const spaces = line.trim().split(/\s+/)
  if (spaces.length === 2) {
    arr1.push(Number(spaces[0]))
    arr2.push(Number(spaces[1]))
  }
})

const result = [arr1, arr2]
console.log("final result\n", result)

const blob = new Blob([JSON.stringify(result)], {type: "application/json"})
const url = URL.createObjectURL(blob);

const a = document.createElement("a")
a.href = url
a.download = "rawDataDog.json"
a.click()

URL.revokeObjectURL(url);
