/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '11/03/2020',
        '11/10/2020',
        '11/17/2020',
        '11/24/2020',
        '12/1/2020',
        '12/8/2020',
        '12/15/2020'
      ],
      datasets: [{
        data: [
          0,
          .04,
          .10,
          .11,
          .18,
          .07,
          .12
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()
