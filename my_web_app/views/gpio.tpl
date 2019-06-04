%rebase('main', title='Input')
<br>
<br>
<h3>Input</h3>
<br>
<h4>{{status}}</h4>
<br>

</form>

<form action="/gpio" method="post">

<label for="tentacles">Eingaben 1 (0-100):</label>
<input type="number" id="tentacles" name="pir_status1"
       min="0" max="100">

<label for="tentacles">+ (0-100):</label>
<input type="number" id="tentacles" name="pir_status2"
       min="0" max="100">

<input type="submit" /><br/>
</form>

 <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
   </head<
   <body>
   <p>Dein Ergebnis</p>
   <p id="data">No data...</p>
   <script language="javascript" type="text/javascript">
   var timeout = setInterval(reloadData, 500);
   function reloadData () {
    $('#data').load('/data2');
   }
   </script>
