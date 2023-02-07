require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/04_#{variation}.txt")
end

def modify(data)
  data.map { |line| line.split(",") }
end

def get_data(variation)
  modify(raw_data(variation))
end

CONTAINES = -> (a, b, c, d) { (a <= c and b >= d) or (c <= a and d >= b) }
OVERLAPS = -> (a, b, c, d) { a.between?(c, d) or c.between?(a, b) }

def easy(data)
  count = 0
  for first_elf, second_elf in data
    a, b = first_elf.split("-").map(&:to_i)
    c, d = second_elf.split("-").map(&:to_i)

    if CONTAINES.call(a, b, c, d)
      count += 1
    end
  end

  count
end

def hard(data)
  count = 0
  for first_elf, second_elf in data
    a, b = first_elf.split("-").map(&:to_i)
    c, d = second_elf.split("-").map(&:to_i)

    if OVERLAPS.call(a, b, c, d)
      count += 1
    end
  end

  count
end

if __FILE__ == $0
  data = get_data(INPUT)
  puts easy(data)
  puts hard(data)
end
