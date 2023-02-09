require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/01_#{variation}.txt",  chomp: true)
end

def modify(data)
  data.slice_when { |element| element == "" }.to_a
      .map { |sub_list| sub_list.map(&:to_i) }
      .map(&:sum)
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
