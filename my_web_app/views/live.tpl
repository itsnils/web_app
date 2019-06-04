%rebase('main', title='Live')
<br>
<br>
<h3>Live aus Python mit Ajax</h3>

<html>
<head><title>Test</title>
   <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
</head>
<body>
<p>Flow Sensor HAFBSF0200C2AX3</p>
<p id="data">No data...</p>
<script language="javascript" type="text/javascript">
   var timeout = setInterval(reloadData, 500);
   function reloadData () {
      $('#data').load('/data');
   }
</script>