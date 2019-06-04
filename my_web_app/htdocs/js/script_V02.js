"use strict";

let ctx = document.getElementById("myChart");

let chart = null ;

let config = {
   type: "line",
   data: {
      labels: [],
      datasets: [{
         label: "Random data",
         backgroundColor: "red",
         borderColor: "red",
         data: [],
         fill: false,
      }]
   },
   options: {
      responsive: true,
      legend: {
         display: false
      },
      tooltips: {
         mode: "index",
         intersect: false,
      },
      hover: {
         mode: "nearest",
         intersect: true
      },
      scales: {
         xAxes: [{
            display: true,
            scaleLabel: {
               display: true,
               labelString: "Point"
            }
         }],
         yAxes: [{
            display: true,
            scaleLabel: {
               display: true,
               labelString: "Value"
            }
         }]
      }
   }
} ;

function update( json )
{
let never = live().done(function (result) {

   let getData = $.getJSON('/value');
   let labels = result.zeit;
   let data = result.flow;

};


}


}

window.onload = () => {
   update() ;
   setInterval( update, 2000 ) ;
} ;