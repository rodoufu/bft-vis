from lxml import objectify

if __name__ == '__main__':
	file_name = 'example/soln4.sol'
	with open(file_name) as file:
		file_content = file.read().encode('utf-8')

		sol = objectify.fromstring(file_content)
		print(
			f"Problem: {sol.header.get('problemName')}, solution: {sol.header.get('solutionName')} has "
			f"{len(sol.variables.variable)} variables, {len(sol.linearConstraints.constraint)} linear constraints"
		)
