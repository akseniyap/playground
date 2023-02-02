require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.open("inputs/01_#{variation}.txt").read
end

def modify(data)
  data.split(NEW_LINE*2)
      .map { |line| line.split.map(&:to_i).sum }
end

def easy(data)
  modify(data).max
end

def hard(data)
  modify(data).sort[-3..-1].sum
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
