#!/bin/sh

output="$1"

python release-graph.py programs.yaml > releases.data
gnuplot <<EOF
set title "OpenStack over Time"
set xdata time
set xlabel "Release date"
set ylabel "Number of programs"
set xtics rotate
set timefmt "%Y-%m-%d"
set terminal svg background "#FFFFFF"
set output "$output"
plot "releases.data" using 1:2 title "Programs in release" with linespoints pt 7
EOF

