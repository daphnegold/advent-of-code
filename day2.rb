puzzle = File.read("./day2.txt")

def surface_area(sides)
  sides.inject(0) { |sum, n| sum + 2 * n[0] * n[1] }
end

def min_side(sides)
  sides.map { |ary| ary[0] * ary [1] }.min
end

total_paper = 0

puzzle.each_line do |dimension|
  sides = dimension.split("x").map(&:to_i).combination(2)
  total_paper += surface_area(sides) + min_side(sides)
end

puts total_paper
