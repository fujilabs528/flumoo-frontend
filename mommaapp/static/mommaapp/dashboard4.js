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
        '11/04/2020',
        '11/05/2020',
        '11/06/2020',
        '11/07/2020',
        '11/08/2020',
        '11/09/2020'
      ],
      datasets: [{
        data: [
          0,
          -.02,
          -.04,
          -.01,
          -.06,
          -.02,
          -.02
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#ff0000',
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
