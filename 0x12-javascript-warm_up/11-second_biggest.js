#!/usr/bin/node
const arr = process.argv
if (arr.length <= 3) { console.log(0) } else {
  arr.sort((a, b) => a - b)
  arr.pop()
  console.log(arr.pop())
}
