require_relative "elf"
require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/04_#{variation}.txt",  chomp: true)
end

def modify(data)
  data.map do |line|
    /(\d+)-(\d+),(\d+)-(\d+)/ =~ line
    [Elf.new($1.to_i, $2.to_i), Elf.new($3.to_i, $4.to_i)]
  end
end

def get_data(variation)
  modify(raw_data(variation))
end

def easy(data)
  count = 0
  data.each do |first_elf, second_elf|
    if first_elf.contains?(second_elf) or second_elf.contains?(first_elf)
      count += 1
    end
  end

  count
end

def hard(data)
  count = 0
  data.each do |first_elf, second_elf|
    if first_elf.overlaps?(second_elf) or second_elf.overlaps?(first_elf)
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
