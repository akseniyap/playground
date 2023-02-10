require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.read("inputs/06_#{variation}.txt").strip
end

def sliding_window(data, n)
  position = n
  data.chars.each_cons(n) do |marker|
    break if marker == marker.uniq
    position += 1
  end

  position
end

def easy(data)
  sliding_window(data, 4)
end

def hard(data)
  sliding_window(data, 14)
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
