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

class Tree
  attr_accessor :x, :y, :height

  def initialize(x, y, height)
    @x = x
    @y = y
    @height = height
  end

  def on_edge?(rows, cols)
    @x == 0 or @y == 0 or @x == cols or @y == rows
  end

  def is_visible?(neighbours)
    neighbours.all? { |tree| @height > tree.height }
  end

  def view_distance(neighbours)
    score = 0
    neighbours.each do |tree|
      score += 1
      if @height <= tree.height
        return score
      end
    end

    score
  end
end

class Board
  attr_accessor :grid

  def initialize
    @grid = []
  end

  def rows
    @grid.size
  end

  def cols
    @grid.first.size
  end

  def get(x, y)
    @grid[y][x]
  end

  def neighbours(tree)
    row = @grid[tree.y]
    col = @grid.collect { |line| line[tree.x] }

    [row[..tree.x-1].reverse, row[tree.x+1..], col[..tree.y-1].reverse, col[tree.y+1..]]
  end

  class << self
    def parse_grid(data)
      board = Board.new
      board.grid = data.map.with_index { |line, j| line.map.with_index { |height, i| Tree.new(i, j, height) } }
      board
    end
  end
end

def easy(data)
  board = Board.parse_grid(data)
  visible_trees = 0

  board.rows.times do |j|
    board.cols.times do |i|
      tree = board.get(i, j)

      if tree.on_edge?(board.rows, board.cols)
        visible_trees += 1
      else
        neighbours = board.neighbours(tree)

        if neighbours.map { |trees| tree.is_visible?(trees) }.any?
          visible_trees += 1
        end
      end
    end
  end

  visible_trees
end

def hard(data)
  board = Board.parse_grid(data)
  view_distances = Array.new(board.rows){ Array.new(board.cols) }

  board.rows.times do |j|
    board.cols.times do |i|
      tree = board.get(i, j)

      if tree.on_edge?(board.rows, board.cols)
        view_distances[j][i] = 0
      else
        neighbours = board.neighbours(tree)
        scores = neighbours.map { |trees| tree.view_distance(trees) }
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
