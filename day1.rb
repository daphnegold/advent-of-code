## Part 1

puzzle = File.read("./day1.txt")

def find_floor(puzzle)
  up = puzzle.count("(")
  down = puzzle.count(")")

  return up - down
end

puts "Santa is on floor #{find_floor(puzzle)}"

## Part 2

current_floor = 0

puzzle.length.times do |i|
  current_slice = puzzle.slice(0..i)
  current_floor = find_floor(current_slice)

  if current_floor == -1
    puts "Santa enters the basement at index #{i + 1}"
    break
  end
end
