/*
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
(Kata 8kyu)
*/

var summation = function (num) {
    soma = 0
    for(i = 0; i <= num; i++){
      soma = soma + i
    }
    return soma
  }