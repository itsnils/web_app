let chart = null ;

let config = {
   type: "line",
   data: {
      labels: [],
      datasets: [{
         label: "Random data",
         //backgroundColor: "red",
         borderColor: "blue",
         data: [],
         fill: false,
         pointRadius: 0,

      }]
   },
   options: {
       animation: {
       duration: 0
   },
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
               labelString: "Time"
            }
         }],
         yAxes: [{
            display: true,
            scaleLabel: {
               display: true,
               labelString: "Flow"
            }
         }],
         yAxes: [{
            ticks: {
                suggestedMin: 0,
                suggestedMax: 1000
            }
        }]

      }
   }
} ;

function update( json )
{
   fetch( "/value" )
         .then( response => response.json() )
         .then( json => {
                          config.data.labels           = json.labels ;
                          config.data.datasets[0].data = json.data ;

                          if( chart === null )
                          {
                             let ctx = document.getElementById( "myChart") ;
                             chart   = new Chart( ctx, config ) ;
                          }
                          else
                          {
                             chart.update() ;
                          }
                        } )
         .catch( error => console.log("Error: "+error) ) ;

}

window.onload = () => {
   update() ;
   setInterval( update, 1000 ) ;
} ;