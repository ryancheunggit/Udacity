/*========Code for Make a Bar Chart I===========*/

/*data to be visualized as bars*/
var data = [4, 8, 15, 16, 23, 42];

/*===Selecting an element====*/

/*create an empty div element*/
var div = document.createElement("div");

/*insert some string values into the div*/
div.innerHTML = "Hello, world!";

/*append the div to the actual page*/
document.body.appendChild(div);

/*use d3 selector*/
var body = d3.select("body");

/*add another div*/
var div = body.append("div");

/*show the same text again*/
div.html("Hello, world!");

/*select all
notice by doing so, we don't have to use loop
*/
var divs = d3.selectAll("div");
divs.html("Hello, walled!");

/*===Chaining methods===*/

/*without using chaining*/
var body = d3.select("body");
body.style("color", "black");
body.style("background-color", "white");

/*with chaining
we even don't need a variable to store body
*/
d3.select("body")
	.style("color", "black")
	.style("background-color", "white");

/*some method return a new selection, eg append*/
d3.selectAll("section")
	.attr("class", "special");
  .append("div")
	.html("Hello, world!");

/*use variable for easy reference*/
var div = d3.selectAll("div");
div.append("p")
	.html("First!");
div.append("p")
	.html("Second!");

/*Coding a Chart Manually*/
/*also see manualChart.html*/
<!DOCTYPE html>
<style>
	.chart div{
		font: 10px sans-serif;
		background-color: steelblue;
		text-align: right;
		padding: 3px;
		margin: 1px;
		color: white;
	}

</style>

<div class = "chart">
	<div style = "width: 40px;">4</div>
	<div style = "width: 80px;">8</div>
	<div style = "width: 150px;">15</div>
	<div style = "width: 160px;">16</div>
	<div style = "width: 230px;">23</div>
	<div style = "width: 420px;">42</div>
</div>


/*Coding a Chart, Automatically*/
/*Start with a empty page with the style in it*/
d3.select("body").append("div").classed("chart", true);
var data = [4, 8, 15, 16, 23, 42];

d3.select(".chart")
  .selectAll("div")
  	.data(data)
  .enter().append("div")
  	.style("width", function(d){return d*10+"px";})
  	.text(function(d){return d;});

/*break it down into pieces*/
var chart = d3.select(".chart");

var bar = chart.selectAll("div");

var barUpdate = bar.data(data);

var barEnter = barUpdate.enter().append("div");

barEnter.style("width", function(d){return d*10+"px";});

barEnter.text(function(d){return d;});

/*===Scaling to Fit===*/
/*rather than fix the scale to be multiple by 10
use the scaling function in d3
*/
var x = d3.scale.linear()
	.domain([0, d3.max(data)])
	.range([0, 420]);

d3.select(".chart")
  .selectAll("div")
  	.data(data)
  .enter().append("div")
  	.style("width", function(d){return x(d)+"px";})
  	.text(function(d){return d;});

/*========Code for Make a Bar Chart II===========*/

/*===Coding a Chart, Manually in SVG===*/
/*also see manualChartSVG.html*/

<!DOCTYPE html>
<style>
	.chart rect{
		fill: steelblue;
	}

	.chart text{
		font: 10px sans-serif;
		text-anchor: end;
		fill: white;
	}
</style>

<svg class = "chart" width = "420" height = "120">
	<g transform = "translate(0,0)">
		<rect width = "40" height = "19"></rect>
		<text x = "37" y = "9.5" dy = ".35em">4</text>
	</g>
	<g transform = "translate(0,20)">
		<rect width = "80" height = "19"></rect>
		<text x = "77" y = "9.5" dy = ".35em">8</text>
	</g>
	<g transform = "translate(0,40)">
		<rect width = "150" height = "19"></rect>
		<text x = "147" y = "9.5" dy = ".35em">15</text>
	</g>
	<g transform = "translate(0,60)">
		<rect width = "160" height = "19"></rect>
		<text x = "157" y = "9.5" dy = ".35em">16</text>
	</g>
	<g transform = "translate(0,80)">
		<rect width = "230" height = "19"></rect>
		<text x = "227" y = "9.5" dy = ".35em">23</text>
	</g>
	<g transform = "translate(0,100)">
		<rect width = "420" height = "19"></rect>
		<text x = "417" y = "9.5" dy = ".35em">42</text>
	</g>
</svg>

/*===Coding a Chart, Automatically in SVG===*/
/*also see automaticChartSVG.html*/

<!DOCTYPE html>
<meta charset = "utf-8">
<style>
	.chart rect{
		fill: steelblue;
	}

	.chart text{
		font: 10px sans-serif;
		text-anchor: end;
		fill: white;
	}
</style>

<svg class = "chart" width = "420" height = "120"></svg>
<script src = "http://d3js.org/d3.v3.min.js" charset = "utf-8"></script>
<script>
	var data = [4, 8, 15, 16, 23, 42];

	var width = 420,
		barHeight = 20;

	var x = d3.scale.linear()
		.domain([0, d3.max(data)])
		.range([0, width]);

	var chart = d3.select(".chart")
		.attr("width", width)
		.attr("height", barHeight * data.length);

	var bar = chart.selectAll("g")
		.data(data)
	  .enter().append("g")
	  	.attr("transform", function(d, i){
	  		return "translate(0," + i * barHeight + ")";});

	bar.append("rect")
		.attr("width", x)
		.attr("height", barHeight - 1);

	bar.append("text")
		.attr("x", function(d){
			return x(d) - 3;
		})
		.attr("y", barHeight / 2)
		.attr("dy", ".35em")
		.text(function(d){return d;});
</script>

/*Loading data from tsv file*/
/*
also see automaticChartSVGfromTSVdata.html
start a python http server at the directory using:
python -m SimpleHTTPServer 8000
and browse using browser as 
http://localhost:8000/automaticChartSVGfromTSVdata.html
*/

<!DOCTYPE html>
<meta charset = "utf-8">
<style>
	.chart rect{
		fill: steelblue;
	}

	.chart text{
		font: 10px sans-serif;
		text-anchor: end;
		fill: white;
	}
</style>

<svg class = "chart"></svg>

<script src = "http://d3js.org/d3.v3.min.js" charset = "utf-8"></script>
<script>

	var width = 420,
		barHeight = 20;

	// don't know the domain yet
	var x = d3.scale.linear()
		.range([0, width]);

	// don't know the height yet
	var chart = d3.select(".chart")
		.attr("width", width);

	// Code inside will only run when data loading is finished
	d3.tsv("data.tsv", type, function(error, data){
		// get the domain from loaded data
		x.domain([0, d3.max(data, function(d){return d.value;})]);
		// calculate the height of bar from data
		chart.attr("height", barHeight * data.length);

		var bar = chart.selectAll("g")
			.data(data)
	  	  .enter().append("g")
	  		.attr("transform", function(d, i){
	  			return "translate(0," + i * barHeight + ")";});

		bar.append("rect")
			.attr("width", function(d){return x(d.value);})
			.attr("height", barHeight - 1);

		bar.append("text")
			.attr("x", function(d){return x(d.value) - 3;})
			.attr("y", barHeight / 2)
			.attr("dy", ".35em")
			.text(function(d){return d.value;});
	});

	function type(d){
		d.value = +d.value;
		return d;
	}


</script>

/*========Code for Make a Bar Chart III===========*/
/*===Rotating into Columns===*/
/*
also see verticalBars.html
start a python http server at the directory using:
python -m SimpleHTTPServer 8000
and browse using browser as 
http://localhost:8000/verticalBars.html
*/

<!DOCTYPE html>
<meta charset = "utf-8">
<style>
	.chart rect{
		fill: steelblue;
	}

	.chart text{
		font: 10px sans-serif;
		text-anchor: middle;
		fill: white;
	}
</style>

<svg class = "chart"></svg>

<script src = "http://d3js.org/d3.v3.min.js" charset = "utf-8"></script>
<script>

	var width = 960,
		height = 500;

	// don't know the domain yet
	var y = d3.scale.linear()
		.range([height, 0]);

	var chart = d3.select(".chart")
		.attr("width", width)
		.attr("height", height);

	// Code inside will only run when data loading is finished
	d3.tsv("data.tsv", type, function(error, data){
		// get the domain from loaded data
		y.domain([0, d3.max(data, function(d){return d.value;})]);
		// calculate the width of bar from data
		var barWidth = width / data.length;

		var bar = chart.selectAll("g")
			.data(data)
	  	  .enter().append("g")
	  		.attr("transform", function(d, i){
	  			return "translate(" + i * barWidth + ",0)";});

		bar.append("rect")
			.attr("y", function(d){return y(d.value);})
			.attr("height", function(d){return height - y(d.value);})
			.attr("width", barWidth - 1);

		bar.append("text")
			.attr("x", barWidth / 2)
			.attr("y", function(d){return y(d.value) + 3;})
			.attr("dy", ".75em")
			.text(function(d){return d.value;});
	});

	function type(d){
		d.value = +d.value;
		return d;
	}

</script>

/*===Encoding Ordinal Data===*/
var x = d3.scale.ordianl()
	.domain(["A","B","C","D","E","F"])
	.range([0,1,2,3,4,5]);

/*use rangeBands 
this will divide the chart area into evenly-spaced, evenly-sized bands.
*/
var x = d3.scale.ordianl()
	.domain(["A","B","C","D","E","F"])
	.rangeBands([0,width]);

/*there is also a rangePoints can be used for scatter plots*/

var x = d3.scale.ordinal()
	.domain(["A","B","C","D","E","F"])
	.rangeRoundBands([0, width], .1);

/*
also see verticalBarsOrdered.html
start a python http server at the directory using:
python -m SimpleHTTPServer 8000
and browse using browser as 
http://localhost:8000/verticalBarsOrdered.html
*/

<!DOCTYPE html>
<meta charset = "utf-8">
<style>
	.chart rect{
		fill: steelblue;
	}

	.chart text{
		font: 10px sans-serif;
		text-anchor: middle;
		fill: white;
	}
</style>

<svg class = "chart"></svg>

<script src = "http://d3js.org/d3.v3.min.js" charset = "utf-8"></script>
<script>

	var width = 960,
		height = 500;

	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width], .1);

	/* compare with this one */
	//var x = d3.scale.ordinal()
	//	.rangeBands([0,width]);

	// don't know the domain yet
	var y = d3.scale.linear()
		.range([height, 0]);

	var chart = d3.select(".chart")
		.attr("width", width)
		.attr("height", height);

	// Code inside will only run when data loading is finished
	d3.tsv("data.tsv", type, function(error, data){
		x.domain(data.map(function(d){return d.name;}));
		// get the domain from loaded data
		y.domain([0, d3.max(data, function(d){return d.value;})]);

		var bar = chart.selectAll("g")
			.data(data)
	  	  .enter().append("g")
	  		.attr("transform", function(d){
	  			return "translate(" + x(d.name) + ",0)";});

		bar.append("rect")
			.attr("y", function(d){return y(d.value);})
			.attr("height", function(d){return height - y(d.value);})
			.attr("width", x.rangeBand());

		bar.append("text")
			.attr("x", x.rangeBand() / 2)
			.attr("y", function(d){return y(d.value) + 3;})
			.attr("dy", ".75em")
			.text(function(d){return d.value;});
	});

	function type(d){
		d.value = +d.value;
		return d;
	}

</script>



/*===Preparing Margins===*/
var margin = {top: 20, right: 30, bottom: 30, left: 40},
	width = 960 - margin.left - margin.right,
	height = 500 - margin.top - margin.bottom;

var chart = d3.select(".chart")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
  .append("g")
  	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// any elements subsequently added to chart will thus inherit the margins  


/*===Adding Axes===*/
var xAxis = d3.svg.axis()
	.scale(x)
	.orient("bottom");

chart.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height +")")
	.call(xAxis);

.axis text {
	font: 10px sans-serif;
}

.axis path,
.axis line{
	fill: none;
	stroke: #000;
	shape-rendering: crispEdges;
}



/*Complete code with axis*/
/*
also see withAxis.html
start a python http server at the directory using:
python -m SimpleHTTPServer 8000
and browse using browser as 
http://localhost:8000/withAxis.html
*/

<!DOCTYPE html>
<meta charset="utf-8">
<style>

.bar {
  fill: steelblue;
}

.axis text {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

</style>
<svg class="chart"></svg>
<script src="//d3js.org/d3.v3.min.js"></script>
<script>

var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("data.tsv", type, function(error, data) {
  x.domain(data.map(function(d) { return d.name; }));
  y.domain([0, d3.max(data, function(d) { return d.value; })]);

  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .call(yAxis);

  chart.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.name); })
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .attr("width", x.rangeBand());
});

function type(d) {
  d.value = +d.value; // coerce to number
  return d;
}

</script>



/*===Communicating===*/
/*
also see final.html
start a python http server at the directory using:
python -m SimpleHTTPServer 8000
and browse using browser as 
http://localhost:8000/final.html
*/

<!DOCTYPE html>
<meta charset="utf-8">
<style>

.bar {
  fill: steelblue;
}

.axis text {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

</style>
<svg class="chart"></svg>
<script src="//d3js.org/d3.v3.min.js"></script>
<script>

var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10, "%");

var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("data.tsv", type, function(error, data) {
  x.domain(data.map(function(d) { return d.name; }));
  y.domain([0, d3.max(data, function(d) { return d.value; })]);

  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .attr("text-anchor", "end")
      .text("Frequency");

  chart.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.name); })
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .attr("width", x.rangeBand());
});

function type(d) {
  d.value = +d.value; // coerce to number
  return d;
}

</script>
