puzzle = File.read("./day1.txt")

up = puzzle.count("(")
down = puzzle.count(")")

floor = up - down

puts floor
