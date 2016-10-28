#!/usr/bin/python

import argparse


def main():
	options = argparse.ArgumentParser(description='Compute oracle performance among runs.')
	required = options.add_argument_group('required arguments')
	required.add_argument('-m', '--metric', help='which metric to optimize', required=True)
	required.add_argument('-f', '--files', help='specify trec_output per-query files to optimize over', required=True, nargs='+')
	options.add_argument('-s', '--summarize', help='report the summary statistic (average)', action='store_true')
	args = options.parse_args()
	
	FILE_KEY = 'file'
	VALUE_KEY = 'value'

	top = {}
	for fil in args.files:
		with open(fil) as f:
			for line in f:
				metric, query, value = line.strip().split()
				if metric.lower() == args.metric and query != 'all' and (query not in top or top[query][VALUE_KEY] < float(value)):
						top[query] = {FILE_KEY: shortest_distinct_file(fil, args.files), VALUE_KEY: float(value)}

	total = 0
	for query in top:
		print('\t'.join([query, '{0:.4f}'.format(top[query][VALUE_KEY]), top[query][FILE_KEY]]))
		total += top[query][VALUE_KEY]
	
	if args.summarize:
		print('\t'.join(['all', '{0:.4f}'.format(total/float(len(top))), '---']))
		

def shortest_distinct_file(fname, files):
	sname = file_only(fname)
	num_match = 0
	for f in files:
		num_match += 1 if file_only(f) == sname else 0
		if num_match > 1:
			return fname
	return sname

def file_only(fname):
	return fname.split('/')[-1].strip()

if __name__ == '__main__':
	main()
