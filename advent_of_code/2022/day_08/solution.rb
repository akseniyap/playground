require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/08_#{variation}.txt",  chomp: true)
end

def modify(data)
  data.map { |line| line.chars.map(&:to_i) }
end

def get_data(variation)
  modify(raw_data(variation))
end

def neighbours(data, i, j)
  row = data[j]
  col = data.collect { |line| line[i] }

  [row[..i-1].reverse, row[i+1..], col[..j-1].reverse, col[j+1..]]
end

def is_visible(current_tree, neighbours)
  neighbours.all? { |tree| current_tree > tree }
end

def view_distance(current_tree, neighbours)
  score = 0
  neighbours.each do |tree|
    score += 1
    if current_tree <= tree
      return score
    end
  end
  score
end

def easy(data)
  visible_trees = 0
  rows = data.size
  cols = data[0].size
  on_edge = -> (i, j) { i == 0 or i == cols - 1 or j == 0 or j == rows - 1 }

  rows.times do |j|
    cols.times do |i|
      current_tree = data[j][i]

      if on_edge.call(i, j)
        visible_trees += 1
      else
        row = data[j]
        col = data.collect { |line| line[i] }
        directions = neighbours(data, i, j)

        if directions.map { |neighbours| is_visible(current_tree, neighbours) }.any?
          visible_trees += 1
        end
      end
    end
  end

  visible_trees
end

def hard(data)
  rows = data.size
  cols = data[0].size
  view_distances = Array.new(rows){ Array.new(cols) }
  on_edge = -> (i, j) { i == 0 or i == cols - 1 or j == 0 or j == rows - 1 }

  rows.times do |j|
    cols.times do |i|
      current_tree = data[j][i]

      if on_edge.call(i, j)
        view_distances[j][i] = 0
      else
        row = data[j]
        col = data.collect { |line| line[i] }
        directions = neighbours(data, i, j)

        scores = directions.map { |neighbours| view_distance(current_tree, neighbours) }
        view_distances[j][i] = scores.inject(:*)
      end
    end
  end

  view_distances.flatten.max
end

if __FILE__ == $0
  data = get_data(INPUT)
  puts easy(data)
  puts hard(data)
end
