// setting up the svg 		
var margin = 50, width = 1080, height = 200, x_axis_space = 100;
var rect_side = 10;

/**
 *	helper function for split the dataset into two subsets based on the gender of the passenger
 *  @param: data file and desired gender for subset
 *  @return: a smaller dataset
*/
function filter_data(data, sex){
	var filtered_data = data.filter(function(d) {
    	return d.Sex === sex;
	});
	return filtered_data;
}

/**
* function for drawing the visualization
* @param: datafile
*/
function drawExploratory(data){

	// subset the dataset
	var male_data = filter_data(data, "male");
	var female_data = filter_data(data, "female"); 

	// set up svgs and append circles
    d3.select("div.exploratory")
    	.append("svg")
    		.attr("width", width)
    		.attr("height", height/2)
    		.attr("class", "male")
     	.selectAll("rect")
    	.data(male_data)
    	.enter()
    	.append("rect");   

    d3.select("div.exploratory")
    	.append("svg")
    		.attr("width", width)
    		.attr("height", height/2 + x_axis_space)
    		.attr("class", "female")
    	.selectAll("rect")
    	.data(female_data)
    	.enter()
    	.append("rect");

   	// build extents 
    var age_extent = d3.extent(data, function(d){
    	return d.Age;
    });

    var pclass_extent = d3.extent(data, function(d){
    	return d.Pclass;
    })

    // build scales
    var x_scale = d3.scale.linear()
    	.range([2.5*margin, width - 2.5*margin])
    	.domain(age_extent);

    var y_scale = d3.scale.linear()
    	.range([rect_side + 10, height/2-margin/2])
    	.domain(pclass_extent);


    // build axis
    var x_axis = d3.svg.axis().scale(x_scale);

    var y_axis = d3.svg.axis().scale(y_scale).orient("left").ticks(2);
    // set positions and radius of points
    d3.selectAll("rect")
    	.attr("x", function(d){return x_scale(d.Age) - rect_side/2;})
    	.attr("y", function(d){return y_scale(d.Pclass) - rect_side/2;})
    	.attr("width",rect_side)
    	.attr("height",rect_side)
    	.attr("opacity", 0.2)
    	.attr("class", function(d){
    		if (d.Survived == 1) return "Survived points";
    		else return "Died points"});

    // add axes labels and legends
    d3.selectAll("svg.female")
    	.append("g")
    		.attr("class", "x_axis")
    		.attr("transform", "translate(0, " + (height/2) + ")")
    		.call(x_axis)

    d3.selectAll("svg.male")
    	.append("g")
    		.attr("transform", "translate(" + (2.5*margin) + ",0)")
    		.attr("class", "y_axes")
    		.call(y_axis);

    d3.selectAll("svg.female")
        .append("g")
            .attr("transform", "translate(" + (2.5*margin) + ",0)")
            .attr("class", "y_axes")
            .call(y_axis);

   
    d3.selectAll("svg.male")
    	.append("g")
    		.attr("class", "y_axis_title")
    		.attr("transform", "translate(" + (2*margin - rect_side) + "," + height/4 +")")
    		.append("text")
    			.attr("text-anchor","middle")
    			.text("Class")
    			.attr("transform", "rotate(270,0,0)");

    d3.selectAll("svg.female")
        .append("g")
            .attr("class", "y_axis_title")
            .attr("transform", "translate(" + (2*margin - rect_side) + "," + height/4 +")")
            .append("text")
                .attr("text-anchor","middle")
                .text("Class")
                .attr("transform", "rotate(270,0,0)");

    d3.select("svg.female")
    	.select("g.y_axes")
    	.append("text")
    		.attr("text-anchor", "left")
    		.text("female")
    		.attr("transform", "translate(" + (-2.4*margin) + "," + height/4 + ")");

    d3.select("svg.male")
    	.select("g.y_axes")
    	.append("text")
    		.attr("text-anchor", "left")
    		.text("male")
    		.attr("transform", "translate(" + (-2.4*margin) + "," + height/4 + ")");

    d3.select("svg.female")
    	.select("g.x_axis")
    	.append("text")
    		.attr("text-anchor", "middle")
    		.text("Age")
    		.attr("transform", "translate(" + width/2 + "," + margin + ")");		   	

    d3.select("svg.male")
    	.append("g")
    		.attr("transform", "translate(" + (width - margin) + "," + height/5 + ")")
    		.attr("class", "survive_legend")
    		.append("rect")
    			.attr("class", "Survived")
    			.attr("width",rect_side)
    			.attr("height",rect_side)
    			.attr("opacity", 1);

    d3.select("g.survive_legend")
    	.append("text")
    		.attr("text-anchor", "middle")
    		.text("Survived")
    		.attr("transform", "translate(" + rect_side/2 + "," + rect_side*2.5 + ")");

    d3.select("svg.female")
    	.append("g")
    		.attr("transform", "translate(" + (width - margin) + "," + height/5 + ")")
    		.attr("class", "die_legend")
    		.append("rect")
    			.attr("class", "Died")
    			.attr("width",rect_side)
    			.attr("height",rect_side)
    			.attr("opacity", 1);

    d3.select("g.die_legend")
    	.append("text")
    		.attr("text-anchor", "middle")
    		.text("Died")
    		.attr("transform", "translate(" + rect_side/2 + "," + rect_side*2.5 + ")");

    // set up tool tip information
    var tip = d3.tip()
		.attr('class', 'd3-tip')
		.offset([-10, 0])
		.html(function(d) {
	    	return "<strong>Gender:</strong> <span style='color:red'>" + d.Sex + "</span>" + " "
	    	 + "<strong>Class:</strong> <span style='color:red'>" + d.Pclass + "</span>" + " "
	    	 + "<strong>Age:</strong> <span style='color:red'>" + d.Age + "</span>" + " " 
	    	 + "<br/>" 
	    	 + "<strong>Survive Rate:</strong> <span style='color:yellow'>" + d.surviveRate + "%" +  "</span>" + " "
	    	 + "<strong>Number of People:</strong> <span style='color:yellow'>" + d.numTotal + "</span>";
	});

	// set up mouse over tool tip information
		d3.selectAll("svg").call(tip);

    d3.selectAll("rect.points")
    	.on("mouseover", tip.show)
    	.on("mouseout", tip.hide);

    // make a separation line
    d3.select("svg.male")
    	.append("line")
    		.attr("x1", ""+0)
    		.attr("y1", ""+(height/2-1))
    		.attr("x2", ""+width)
    		.attr("y2", ""+(height/2-1))
    		.attr("stroke", "black")
    		.attr("opacity", 0.5);
}