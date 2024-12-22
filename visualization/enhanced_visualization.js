// Pre-PPO Visualizations
function createPrePPOCharts(data) {
    const container = d3.select("#prePpoChart");
    container.html(""); // Clear previous charts

    // IPC Progression Chart
    createLineChart(data, "Iteration", "IPC", "#prePpoChart", "IPC Progression Over Iterations");

    // Scatter Plot: IPC vs. Memory Usage
    createScatterPlot(data, "Memory_Usage", "IPC", "#prePpoChart", "IPC vs Memory Usage");

    // Cache Hit Rate Over Iterations
    createBarChart(data, "Iteration", "Cache_Hit_Rate", "#prePpoChart", "Cache Hit Rate Over Iterations");
}

// Line Chart Function
function createLineChart(data, xKey, yKey, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 400);

    const xScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d[xKey]))
        .range([50, 750]);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d[yKey])])
        .range([350, 50]);

    svg.append("g")
        .attr("transform", "translate(0,350)")
        .call(d3.axisBottom(xScale));

    svg.append("g")
        .attr("transform", "translate(50,0)")
        .call(d3.axisLeft(yScale));

    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "blue")
        .attr("stroke-width", 2)
        .attr("d", d3.line()
            .x(d => xScale(d[xKey]))
            .y(d => yScale(d[yKey]))
        );

    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Scatter Plot Function
function createScatterPlot(data, xKey, yKey, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 400);

    const xScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d[xKey]))
        .range([50, 750]);

    const yScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d[yKey]))
        .range([350, 50]);

    svg.append("g")
        .attr("transform", "translate(0,350)")
        .call(d3.axisBottom(xScale));

    svg.append("g")
        .attr("transform", "translate(50,0)")
        .call(d3.axisLeft(yScale));

    svg.selectAll(".dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", d => xScale(d[xKey]))
        .attr("cy", d => yScale(d[yKey]))
        .attr("r", 5)
        .attr("fill", "orange");

    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Bar Chart Function
function createBarChart(data, xKey, yKey, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 400);

    const xScale = d3.scaleBand()
        .domain(data.map(d => d[xKey]))
        .range([50, 750])
        .padding(0.1);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d[yKey])])
        .range([350, 50]);

    svg.append("g")
        .attr("transform", "translate(0,350)")
        .call(d3.axisBottom(xScale));

    svg.append("g")
        .attr("transform", "translate(50,0)")
        .call(d3.axisLeft(yScale));

    svg.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", d => xScale(d[xKey]))
        .attr("y", d => yScale(d[yKey]))
        .attr("width", xScale.bandwidth())
        .attr("height", d => 350 - yScale(d[yKey]))
        .attr("fill", "green");

    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Function to render all Post-PPO charts in a single container
function createPostPPOCharts(data) {
    const container = d3.select("#postPpoChart");
    container.html(""); // Clear previous charts

    // Render Reward Distribution Histogram
    createRewardHistogram(data, "Reward", "#postPpoChart", "Reward Distribution by Iteration");

    // Render Interactive Bubble Chart
    createInteractiveBubbleChart(data, "#postPpoChart", "Interactive Bubble Chart: IPC vs Reward");

    // Render Correlation Heatmap
    const keys = ["IPC", "Reward", "Action_Prob_InOrder", "Action_Prob_OutOrder"];
    createHeatmap(data, keys, "#postPpoChart", "Correlation Heatmap: Post-PPO Metrics");
}

// Reward Histogram Function
function createRewardHistogram(data, key, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 400);

    const bins = d3.bin()
        .domain(d3.extent(data, d => d[key]))
        .thresholds(20)(data.map(d => d[key]));

    const xScale = d3.scaleLinear()
        .domain([bins[0].x0, bins[bins.length - 1].x1])
        .range([50, 750]);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(bins, d => d.length)])
        .range([350, 50]);

    svg.append("g")
        .attr("transform", "translate(0,350)")
        .call(d3.axisBottom(xScale).ticks(10));

    svg.append("g")
        .attr("transform", "translate(50,0)")
        .call(d3.axisLeft(yScale).ticks(10));

    svg.selectAll("rect")
        .data(bins)
        .enter()
        .append("rect")
        .attr("x", d => xScale(d.x0))
        .attr("y", d => yScale(d.length))
        .attr("width", d => xScale(d.x1) - xScale(d.x0) - 1)
        .attr("height", d => 350 - yScale(d.length))
        .attr("fill", "steelblue");

    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Interactive Bubble Chart Function
function createInteractiveBubbleChart(data, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 400);

    const xScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d.IPC))
        .range([50, 750]);

    const yScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d.Reward))
        .range([350, 50]);

    const sizeScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.Action_Prob_OutOrder)])
        .range([5, 20]);

    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    svg.append("g")
        .attr("transform", "translate(0,350)")
        .call(d3.axisBottom(xScale).ticks(10));

    svg.append("g")
        .attr("transform", "translate(50,0)")
        .call(d3.axisLeft(yScale).ticks(10));

    const tooltip = d3.select("body")
        .append("div")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("background", "#fff")
        .style("border", "1px solid #ccc")
        .style("padding", "10px")
        .style("border-radius", "5px");

    svg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", d => xScale(d.IPC))
        .attr("cy", d => yScale(d.Reward))
        .attr("r", d => sizeScale(d.Action_Prob_OutOrder))
        .attr("fill", d => colorScale(d.Selected_Action))
        .attr("opacity", 0.7)
        .on("mouseover", function (event, d) {
            tooltip.html(`
                <strong>Iteration:</strong> ${d.Iteration}<br>
                <strong>IPC:</strong> ${d.IPC}<br>
                <strong>Reward:</strong> ${d.Reward}<br>
                <strong>Selected Action:</strong> ${d.Selected_Action}<br>
                <strong>Action Prob (OutOrder):</strong> ${d.Action_Prob_OutOrder.toFixed(2)}
            `);
            tooltip.style("visibility", "visible");
        })
        .on("mousemove", function (event) {
            tooltip.style("top", `${event.pageY - 10}px`).style("left", `${event.pageX + 10}px`);
        })
        .on("mouseout", function () {
            tooltip.style("visibility", "hidden");
        });

    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Load Pre-PPO dataset
d3.csv("pre_ppo_dataset.csv").then(function (data) {
    data.forEach(d => {
        d.Iteration = +d.Iteration;
        d.IPC = +d.IPC;
        d.Memory_Usage = +d.Memory_Usage;
        d.Cache_Hit_Rate = +d.Cache_Hit_Rate;
    });

    const algorithms = [...new Set(data.map(d => d.Algorithm))];

    // Dropdown for algorithm filtering
    const dropdown = d3.select("#prePpoFilter")
        .append("select")
        .on("change", function () {
            const selectedAlgorithm = d3.select(this).property("value");
            const filteredData = data.filter(d => d.Algorithm === selectedAlgorithm);
            createPrePPOCharts(filteredData);
        });

    dropdown.selectAll("option")
        .data(algorithms)
        .enter()
        .append("option")
        .text(d => d)
        .attr("value", d => d);

    // Initial chart rendering
    createPrePPOCharts(data.filter(d => d.Algorithm === algorithms[0]));
});

// Function to create a heatmap for Post-PPO Correlations
function createHeatmap(data, keys, target, title) {
    const svg = d3.select(target)
        .append("svg")
        .attr("width", 800)
        .attr("height", 1000);

    // Prepare correlation matrix
    const matrix = [];
    keys.forEach((key1, i) => {
        keys.forEach((key2, j) => {
            const values1 = data.map(d => d[key1]);
            const values2 = data.map(d => d[key2]);
            const correlation = d3.corr(values1, values2); // Custom correlation calculation
            matrix.push({ x: i, y: j, value: correlation });
        });
    });

    // Create scales
    const scale = d3.scaleLinear()
        .domain([-1, 1]) // Correlation range
        .range(["blue", "white", "red"]);

    const size = 155;
    const padding = 200;

    // Render heatmap cells
    svg.selectAll("rect")
        .data(matrix)
        .enter()
        .append("rect")
        .attr("x", d => d.x * size + padding)
        .attr("y", d => d.y * size + padding)
        .attr("width", size)
        .attr("height", size)
        .attr("fill", d => scale(d.value));

    // Add labels for axes
    keys.forEach((key, i) => {
        svg.append("text")
            .attr("x", i * size + padding + size / 2)
            .attr("y", padding - 10)
            .attr("text-anchor", "middle")
            .text(key);

        svg.append("text")
            .attr("x", padding - 10)
            .attr("y", i * size + padding + size / 2)
            .attr("text-anchor", "end")
            .attr("alignment-baseline", "middle")
            .text(key);
    });

    // Add title
    svg.append("text")
        .attr("x", 400)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .text(title);
}

// Custom function to calculate correlation
d3.corr = function (a, b) {
    const meanA = d3.mean(a);
    const meanB = d3.mean(b);
    const num = d3.sum(a.map((x, i) => (x - meanA) * (b[i] - meanB)));
    const den = Math.sqrt(
        d3.sum(a.map(x => Math.pow(x - meanA, 2))) *
        d3.sum(b.map(x => Math.pow(x - meanB, 2)))
    );
    return num / den;
};

// Update Post-PPO visualizations to include heatmap
d3.csv("ppo_results.csv").then(function (data) {
    data.forEach(d => {
        d.Iteration = +d.Iteration;
        d.IPC = +d.IPC;
        d.Reward = +d.Reward;
        d.Action_Prob_InOrder = +d.Action_Prob_InOrder;
        d.Action_Prob_OutOrder = +d.Action_Prob_OutOrder;
    });

    // Create heatmap with selected keys
    const keys = ["IPC", "Reward", "Action_Prob_InOrder", "Action_Prob_OutOrder"];
    createHeatmap(data, keys, "#postPpoChart", "Correlation Heatmap: Post-PPO Metrics");

    // Other Post-PPO visualizations
    createPostPPOCharts(data);
});





