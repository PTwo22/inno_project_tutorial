# Week 11 - React D3 Demo: Setup and Code Explanation

[TOC]

# Part B of Week 11:

This guide will walk you through setting up and understanding the React D3 demo project, which showcases various types of interactive D3 charts within a React application.

## Project Setup

1. Create a new React project:
   ```
   npx create-react-app react-d3-demo
   cd react-d3-demo
   ```

2. Install necessary dependencies:
   ```
   npm install d3
   ```

3. Replace the contents of `src/App.js` from demo, create a new file `src/D3Chart.js`, and add a `barChartData.json` file in the `public/data/` directory with the provided content.

   * The **barChartData.json** file should be created in the correct path, which is `public/data/`. This JSON file will contain the following data:

   ```json
   [
     { "category": "A", "value": 30 },
     { "category": "B", "value": 80 },
     { "category": "C", "value": 45 },
     { "category": "D", "value": 60 },
     { "category": "E", "value": 20 },
     { "category": "F", "value": 90 },
     { "category": "G", "value": 50 }
   ]
   ```

   

## File Structure

- `src/App.js`: Main application component
- `src/D3Chart.js`: Reusable D3 chart component
- `public/data/barChartData.json`: Data for the bar chart

## Code Explanation

### App.js

```javascript
import React, { useState } from 'react';
import D3Chart from './D3Chart';
import './App.css';

function App() {
  const [chartType, setChartType] = useState('sunburst');

  return (
    <div className="App">
      <header className="App-header">
        <h1>Advanced Interactive D3 Charts in React</h1>
        <select 
          value={chartType} 
          onChange={(e) => setChartType(e.target.value)}
          className="chart-selector"
        >
          <option value="multiline">Multi-dimensional Line Chart</option>
          <option value="interactive-pie">Interactive Pie Chart</option>
          <option value="sunburst">Zoomable Sunburst</option>
          <option value="bar">Bar Chart (Fetch Data from the file) </option>
        </select>
        <div className="chart-container">
          <D3Chart type={chartType} />
        </div>
      </header>
    </div>
  );
}

export default App;
```

This component:
- Uses the `useState` hook to manage the selected chart type.
- Renders a dropdown menu to select different chart types.
- Passes the selected chart type to the `D3Chart` component.

### D3Chart.js

This file contains the main logic for rendering different types of D3 charts. Let's break it down:

1. Imports and initial setup:
   ```javascript
   import React, { useRef, useEffect, useState } from 'react';
   import * as d3 from 'd3';
   ```
   - We import necessary hooks from React and the entire D3 library.

     
   
2. Component definition and state management:
   ```javascript
   const D3Chart = ({ type }) => {
     const chartRef = useRef();
     const [data, setData] = useState([
       { name: 'A', value: 30, x: 10, y: 20 },
       { name: 'B', value: 50, x: 20, y: 40 },
       { name: 'C', value: 20, x: 30, y: 10 },
       { name: 'D', value: 40, x: 40, y: 30 },
       { name: 'E', value: 60, x: 50, y: 50 },
     ]);
     const [fileData, setFileData] = useState(null);
     const [isLoading, setIsLoading] = useState(false);
     const [error, setError] = useState(null);
     const [dimensions, setDimensions] = useState(['x', 'y']);
     const sunburstData = {
       name: "root",
       children: [
         {
           name: "parent A",
           children: [
             { name: "child A1", value: 10 },
             { name: "child A2", value: 15 },
           ],
         },
         {
           name: "parent B",
           children: [
             { name: "child B1", value: 20 },
             { name: "child B2", value: 25 },
           ],
         },
         {
           name: "parent C",
           children: [
             { name: "child C1", value: 30 },
             { name: "child C2", value: 35 },
           ],
         },
       ],
     };
   ```
   - This component renders different chart types using D3.js in a React app. 
   - It manages data, dimensions, and loading states with useState, and references the chart DOM element with useRef. 
   - The initial data includes coordinates and values, while sunburstData provides a hierarchy for a sunburst chart. The type prop controls which chart to render, making the component flexible for different visualizations.
   
   3. Data fetching for bar chart:
   
   ```javascript
   useEffect(() => {
       if (type === 'bar') {
         setIsLoading(true);
         setError(null);
         fetch('/data/barChartData.json')
           .then(response => {
             if (!response.ok) {
               throw new Error('Network response was not ok');
             }
             return response.json();
           })
           .then(data => {
             setFileData(data);
             setIsLoading(false);
           })
           .catch(error => {
             console.error('Error loading the bar chart data:', error);
             setError(error.message);
             setIsLoading(false);
           });
       }
     }, [type]);
   ```
   - This effect hook fetches data for the bar chart when the chart type is 'bar'.
   
     
   
4. Main chart rendering logic:
   ```javascript
   useEffect(() => {
       // Clear previous chart
       d3.select(chartRef.current).selectAll('*').remove();
     
       const container = d3.select(chartRef.current);
       const width = container.node().getBoundingClientRect().width;
       const height = container.node().getBoundingClientRect().height;
     
       const svg = container.append('svg')
         .attr('width', '100%')
         .attr('height', '100%')
         .attr('viewBox', `0 0 ${width} ${height}`)
         .style('font', '10px sans-serif');
     
       switch (type) {
         case 'multiline':
           drawMultiLineChart(svg, width, height);
           break;
         case 'interactive-pie':
           drawInteractivePieChart(svg, width, height);
           break;
         case 'sunburst':
           drawZoomableSunburst(svg, width, height);
           break;
         case 'bar':
           if (fileData && fileData.length > 0) {
             drawBarChart(svg, width, height);
           }
           break;
         default:
           break;
       }
     }, [type, data, dimensions, fileData]);
   
   
     const drawBarChart = (svg, width, height) => {
       const margin = { top: 20, right: 20, bottom: 30, left: 40 };
       const innerWidth = width - margin.left - margin.right;
       const innerHeight = height - margin.top - margin.bottom;
   
       const x = d3.scaleBand()
         .range([0, innerWidth])
         .padding(0.1);
   
       const y = d3.scaleLinear()
         .range([innerHeight, 0]);
   
       const g = svg.append('g')
         .attr('transform', `translate(${margin.left},${margin.top})`);
   
       x.domain(fileData.map(d => d.category));
       y.domain([0, d3.max(fileData, d => d.value)]);
   
       g.append('g')
         .attr('transform', `translate(0,${innerHeight})`)
         .call(d3.axisBottom(x));
   
       g.append('g')
         .call(d3.axisLeft(y));
   
       g.selectAll('.bar')
         .data(fileData)
         .enter().append('rect')
         .attr('class', 'bar')
         .attr('x', d => x(d.category))
         .attr('width', x.bandwidth())
         .attr('y', d => y(d.value))
         .attr('height', d => innerHeight - y(d.value))
         .attr('fill', 'steelblue');
     };
   
   
     const drawMultiLineChart = (svg, width, height) => {
       const margin = { top: 20, right: 20, bottom: 30, left: 50 };
       const innerWidth = width - margin.left - margin.right;
       const innerHeight = height - margin.top - margin.bottom;
   
       const g = svg.append('g')
         .attr('transform', `translate(${margin.left},${margin.top})`);
   
       const x = d3.scaleLinear().range([0, innerWidth]);
       const y = d3.scaleLinear().range([innerHeight, 0]);
   
       const line = d3.line()
         .x(d => x(d[dimensions[0]]))
         .y(d => y(d[dimensions[1]]));
   
       x.domain(d3.extent(data, d => d[dimensions[0]]));
       y.domain(d3.extent(data, d => d[dimensions[1]]));
   
       g.append('g')
         .attr('transform', `translate(0,${innerHeight})`)
         .call(d3.axisBottom(x));
   
       g.append('g')
         .call(d3.axisLeft(y));
   
       g.append('path')
         .datum(data)
         .attr('fill', 'none')
         .attr('stroke', 'steelblue')
         .attr('stroke-width', 1.5)
         .attr('d', line);
   
       g.selectAll('.dot')
         .data(data)
         .enter().append('circle')
         .attr('class', 'dot')
         .attr('cx', d => x(d[dimensions[0]]))
         .attr('cy', d => y(d[dimensions[1]]))
         .attr('r', 5)
         .attr('fill', 'steelblue');
   
       // Add dimension selectors
       const dimensionSelector = (index) => {
         const select = d3.select(chartRef.current)
           .append('select')
           .on('change', function() {
             dimensions[index] = this.value;
             setDimensions([...dimensions]);
           });
   
         select.selectAll('option')
           .data(Object.keys(data[0]).filter(k => k !== 'name'))
           .enter().append('option')
           .attr('value', d => d)
           .text(d => d)
           .property('selected', d => d === dimensions[index]);
       };
   
       dimensionSelector(0);
       dimensionSelector(1);
     };
   
     const drawInteractivePieChart = (svg, width, height) => {
       const radius = Math.min(width, height) / 2;
   
       const color = d3.scaleOrdinal(d3.schemeCategory10);
   
       const pie = d3.pie()
         .value(d => d.value)
         .sort(null);
   
       const arc = d3.arc()
         .innerRadius(radius * 0.4)
         .outerRadius(radius * 0.8);
   
       const outerArc = d3.arc()
         .innerRadius(radius * 0.9)
         .outerRadius(radius * 0.9);
   
       const g = svg.append('g')
         .attr('transform', `translate(${width / 2},${height / 2})`);
   
       const arcs = g.selectAll('.arc')
         .data(pie(data))
         .enter().append('g')
         .attr('class', 'arc');
   
       arcs.append('path')
         .attr('d', arc)
         .attr('fill', d => color(d.data.name))
         .attr('stroke', 'white')
         .style('stroke-width', '2px')
         .style('opacity', 0.7)
         .on('mouseover', function(event, d) {
           d3.select(this)
             .style('opacity', 1)
             .transition()
             .duration(200)
             .attr('d', d3.arc().innerRadius(radius * 0.4).outerRadius(radius * 0.85));
         })
         .on('mouseout', function(event, d) {
           d3.select(this)
             .style('opacity', 0.7)
             .transition()
             .duration(200)
             .attr('d', arc);
         });
   
       const text = arcs.append('text')
         .attr('transform', d => `translate(${outerArc.centroid(d)})`)
         .attr('dy', '.35em');
   
       text.append('tspan')
         .attr('x', 0)
         .attr('y', '-0.7em')
         .style('font-weight', 'bold')
         .text(d => d.data.name);
   
       text.append('tspan')
         .attr('x', 0)
         .attr('y', '1em')
         .text(d => d.data.value);
   
       arcs.selectAll('polyline')
         .data(pie(data))
         .enter()
         .append('polyline')
         .attr('points', function(d) {
           const pos = outerArc.centroid(d);
           return [arc.centroid(d), outerArc.centroid(d), pos];
         })
         .style('fill', 'none')
         .style('stroke', 'black')
         .style('stroke-width', '1px');
     };
   
     const drawZoomableSunburst = (svg, width, height) => {
       const radius = Math.min(width, height) / 10;
       const color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, sunburstData.children.length + 1));
   
       const partition = data => {
           const root = d3.hierarchy(data)
               .sum(d => d.value)
               .sort((a, b) => b.value - a.value);
           return d3.partition()
               .size([2 * Math.PI, root.height + 1])
             (root);
         };
     
         const root = partition(sunburstData);
         root.each(d => d.current = d);
     
         const arc = d3.arc()
             .startAngle(d => d.x0)
             .endAngle(d => d.x1)
             .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
             .padRadius(radius * 1.5)
             .innerRadius(d => d.y0 * radius)
             .outerRadius(d => Math.max(d.y0 * radius, d.y1 * radius - 1));
     
         const g = svg.append('g')
             .attr('transform', `translate(${width / 2},${height / 2})`);
     
         const path = g.append('g')
           .selectAll('path')
           .data(root.descendants().slice(1))
           .join('path')
             .attr('fill', d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })
             .attr('fill-opacity', d => arcVisible(d.current) ? (d.children ? 0.6 : 0.4) : 0)
             .attr('pointer-events', d => arcVisible(d.current) ? 'auto' : 'none')
             .attr('d', d => arc(d.current));
     
         path.filter(d => d.children)
             .style('cursor', 'pointer')
             .on('click', clicked);
     
         const label = g.append('g')
             .attr('pointer-events', 'none')
             .attr('text-anchor', 'middle')
             .style('user-select', 'none')
           .selectAll('text')
           .data(root.descendants().slice(1))
           .join('text')
             .attr('dy', '0.35em')
             .attr('fill-opacity', d => +labelVisible(d.current))
             .attr('transform', d => labelTransform(d.current))
             .text(d => d.data.name);
     
         const parent = g.append('circle')
             .datum(root)
             .attr('r', radius)
             .attr('fill', 'none')
             .attr('pointer-events', 'all')
             .on('click', clicked);
     
         function clicked(event, p) {
           parent.datum(p.parent || root);
     
           root.each(d => d.target = {
             x0: Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
             x1: Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
             y0: Math.max(0, d.y0 - p.depth),
             y1: Math.max(0, d.y1 - p.depth)
           });
     
           const t = g.transition().duration(750);
     
           path.transition(t)
               .tween('data', d => {
                 const i = d3.interpolate(d.current, d.target);
                 return t => d.current = i(t);
               })
             .filter(function(d) {
               return +this.getAttribute('fill-opacity') || arcVisible(d.target);
             })
               .attr('fill-opacity', d => arcVisible(d.target) ? (d.children ? 0.6 : 0.4) : 0)
               .attr('pointer-events', d => arcVisible(d.target) ? 'auto' : 'none')
               .attrTween('d', d => () => arc(d.current));
     
           label.filter(function(d) {
               return +this.getAttribute('fill-opacity') || labelVisible(d.target);
             }).transition(t)
               .attr('fill-opacity', d => +labelVisible(d.target))
               .attrTween('transform', d => () => labelTransform(d.current));
         }
     
         function arcVisible(d) {
           return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
         }
     
         function labelVisible(d) {
           return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
         }
     
         function labelTransform(d) {
           const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
           const y = (d.y0 + d.y1) / 2 * radius;
           return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
         }
       };
   
       return <div ref={chartRef} style={{ width: '700px', height: '500px' }}></div>;
   };
   
   export default D3Chart;
   ```
   - This code defines a D3Chart component in React that renders various types of charts (multiline, interactive pie, sunburst, and bar charts) using D3.js. 
   
   - The useEffect hook ensures that any previously drawn chart is cleared before rendering a new one based on the type prop. 
   
   - Depending on the type of chart selected, it calls specific functions to draw the chart, such as drawBarChart, drawMultiLineChart, drawInteractivePieChart, or drawZoomableSunburst. 
   
   - Each of these functions creates the chart by manipulating the SVG elements and scaling the data to fit within the chart’s dimensions.
   
     
   
5. Individual chart drawing functions:
   - `drawBarChart`: Renders a bar chart using data fetched from a file.
   - `drawMultiLineChart`: Renders a multi-dimensional line chart with selectable dimensions.
   - `drawInteractivePieChart`: Renders an interactive pie chart with hover effects.
   - `drawZoomableSunburst`: Renders a zoomable sunburst chart.

Each of these functions uses D3.js to create the respective chart types, setting up scales, axes, and interactive elements as needed.

## Running the Application

1. Start the development server:
   ```
   npm start
   ```

2. Open your browser and navigate to `http://localhost:3000`.

3. Use the dropdown menu to switch between different chart types.

## Customization

You can customize this application by:
- Adding new chart types in the `D3Chart` component.
- Modifying the existing chart drawing functions to change their appearance or behavior.
- Adding more data sources or changing the existing data structure.

## Troubleshooting

If you encounter any issues:
- Ensure all dependencies are correctly installed.
- Check the browser console for any error messages.
- Verify that the `barChartData.json` file is correctly placed in the `public/data/` directory.

Enjoy exploring and customizing your React D3 demo!
