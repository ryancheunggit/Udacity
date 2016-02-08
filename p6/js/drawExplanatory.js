// setting up the svg 		
var margin2 = {top: 20, right: 20, bottom: 30, left: 40},
    width2 = 600 - margin2.left - margin2.right,
    height2 = 400 - margin2.top - margin2.bottom;

// build scales
var x0 = d3.scale.ordinal()
    .rangeRoundBands([40, width2], .1);

var x1 = d3.scale.ordinal();

var y = d3.scale.linear()
    .range([height2, 0]);

var color = d3.scale.ordinal()
    .range(["#98abc5", "#8a89a6", "#7b6888"]);

// build axis
var xAxis = d3.svg.axis()
    .scale(x0)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

// bind bars to the svg element
var svg = d3.select(".explanatory").append("svg")
	.attr("class", "groupedBar")
    .attr("width", width2 + margin2.left + margin2.right)
    .attr("height", height2 + margin2.top + margin2.bottom);

// load data and draw the visualization
d3.csv("sdata.csv", function(error, data) {

	// get the plcass names
	var classNames = d3.keys(data[0]).filter(function(key) { return key !== "Sex"; });

	// convert the data value into numerical type
	data.forEach(function(d) {
		d.rates = classNames.map(function(name) { return {name: name, value: +d[name]}; });
	});

	// refine scales
	x0.domain(data.map(function(d) { return d.Sex; }));
	x1.domain(classNames).rangeRoundBands([0, x0.rangeBand()]);
	y.domain([0, d3.max(data, function(d) { return d3.max(d.rates, function(d) { return d.value; }); })]);

	// append axes and labels
	svg.append("g")
	  .attr("class", "x_axes")
	  .attr("transform", "translate(0," + height2 + ")")
	  .call(xAxis);

	svg.append("g")
	  .attr("class", "yaxes")
	  .attr("transform", "translate(30,0)")
	  .call(yAxis)
	.append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", 6)
	  .attr("dy", ".71em")
	  .style("text-anchor", "end")
	  .text("Surviving Rate (%)");

	// add gender labels
	var sex = svg.selectAll(".sex")
	  .data(data)
	.enter().append("g")
	  .attr("class", "sex")
	  .attr("transform", function(d) { return "translate(" + x0(d.Sex) + ",0)"; });

	// add bars
	sex.selectAll("rect")
	  .data(function(d) { return d.rates; })
	.enter().append("rect")
	  .attr("width", x1.rangeBand())
	  .attr("x", function(d) { return x1(d.name); })
	  .attr("y", function(d) { return y(d.value); })
	  .attr("height", function(d) { return height2 - y(d.value); })
	  .style("fill", function(d) { return color(d.name); });

	// set up legned
	var legend = svg.selectAll(".legend")
	  .data(classNames.slice())
	.enter().append("g")
	  .attr("class", "legend")
	  .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

	legend.append("rect")
	  .attr("x", width2 - 18)
	  .attr("width", 18)
	  .attr("height", 18)
	  .style("fill", color);

	legend.append("text")
	  .attr("x", width2 - 24)
	  .attr("y", 9)
	  .attr("dy", ".35em")
	  .style("text-anchor", "end")
	  .text(function(d) { return d; });

});