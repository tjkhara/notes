func round(n) {
	n = n + 0.5
	n = int(n)
	return n
}

/^h/ && $2 > 500 {print $1,$2,round($2/100)"K"}
