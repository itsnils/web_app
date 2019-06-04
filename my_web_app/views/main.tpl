<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>
      {{title}}
    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link href="/static/css/bootstrap.css" rel="stylesheet">
    <link href="/static/css/bootstrap-theme.css" rel="stylesheet">
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="/static/js/bootstrap.js"></script>
    <body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">The device</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="/index">Live Chart</a></li>  <!-- TODO balke obe isch diker wie suscht. -->
            <li><a href="/settings">Settings</a></li>
            <li><a href="/gpio">Eingabe</a></li>
            <li><a href="/live">Flow Sensor</a></li>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <div class="container">
        <div class="starter-template">
            {{!base}}
        </div>
    </div><!-- /.container -->
    </body>
</html>