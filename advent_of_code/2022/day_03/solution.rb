require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/03_#{variation}.txt",  chomp: true)
end

LETTERS = [*('a'..'z'), *('A'..'Z')]

COMMON_ITEM = -> list { list.map(&:chars).inject(:&)[0] }
PRIORITY = -> (el) { LETTERS.find_index(el) + 1 }

def easy(data)
  compartments = data.map { |el| [el[..el.size/2], el[el.size/2..]] }
  common_items = compartments.map { |el| COMMON_ITEM.call(el) }
  priorities = common_items.map { |el| PRIORITY.call(el) }

  priorities.sum
end

def hard(data)
  groups = data.each_slice(3).to_a
  common_items = groups.map { |el| COMMON_ITEM.call(el) }
  priorities = common_items.map { |el| PRIORITY.call(el) }

  priorities.sum
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
